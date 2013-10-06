from dragonfly.all import Grammar, CompoundRule
from time import *
from threading import Timer
from datetime import datetime
import pythoncom, time
import playbackController as pc

global latencyBuffer
latencyBuffer = 1.0
global times
times = {}
global timers
timers = {}
global tempoGuess
tempoGuess = 0.0

def computeTempo():
  global tempoGuess, times
  deltas = []
  for i, later in times.iteritems():
    for j, earlier in times.iteritems():
      if i > j:
        diff = later - earlier
        total = diff.seconds + (float(diff.microseconds) / 1000000)
        deltas.append(total / float(i - j))
  ave = avg(deltas)
  tempoGuess = ave

def avg(deltas):
  total = 0
  for delta in deltas:
    total += delta
  return float(total) / len(deltas)

def tryTimer(index):
  global tempoGuess, latencyBuffer, timers
  for i, timer in timers.iteritems():
    timer.cancel()
  t = float(4 - index) * tempoGuess
  timers[index] = Timer(max(t - latencyBuffer, 0), Tempo().startLoop)
  timers[index].start()

class Tempo():

  class One(CompoundRule):
    spec = "one"

    def _process_recognition(self, node, extras):
      print "One"
      global times
      times[0] = datetime.now()

  class Two(CompoundRule):
    spec = "(two | Two)"
    
    def _process_recognition(self, node, extras):
      print "Two"
      global times
      times[1] = datetime.now()
      if len(times) >= 2:
        computeTempo()
        tryTimer(1)

  class Three(CompoundRule):
    spec = "three"
    def _process_recognition(self, node, extras):
      print "Three"
      global times
      times[2] = datetime.now()
      if len(times) >= 2:
        computeTempo()
        tryTimer(2)

  class Four(CompoundRule):
    spec = "four"
    def _process_recognition(self, node, extras):
      print "Four"
      times[3] = datetime.now()
      if len(times) >= 2:
        computeTempo()
        tryTimer(3)

  def startLoop(self):
    pc.setTempo(tempoGuess)
    pc.setGenre("rock")
    pc.loop()

    grammar = Grammar("countdown")
    grammar.add_rule(Tempo().One())
    grammar.add_rule(Tempo().Two())
    grammar.add_rule(Tempo().Three())
    grammar.add_rule(Tempo().Four())
    grammar.unload()

grammar = Grammar("countdown")
grammar.add_rule(Tempo().One())
grammar.add_rule(Tempo().Two())
grammar.add_rule(Tempo().Three())
grammar.add_rule(Tempo().Four())
grammar.load()

while True:
  pythoncom.PumpWaitingMessages()
  time.sleep(.1)