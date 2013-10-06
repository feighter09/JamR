from dragonfly.all import Grammar, CompoundRule
from time import *
from datetime import datetime
import pythoncom, time
# import sequencer

class tempoOne(CompoundRule):
    spec = "one"
    def _process_recognition(self, node, extras):
        print "One"
        one()

class tempoTwo(CompoundRule):
    spec = "two"
    def _process_recognition(self, node, extras):
        print "Two"
        two()

class tempoThree(CompoundRule):
    spec = "three"
    def _process_recognition(self, node, extras):
        print "Three"
        three()

class tempoFour(CompoundRule):
    spec = "four"
    def _process_recognition(self, node, extras):
        print "four"
        four()

def avg(deltas):
    total = 0
    for delta in deltas:
        total += delta
    return float(total) / len(deltas)

def startLoop():
    beat = float(avg(timeDeltas)) / 4
    i = 0
    while True:    
        sendBeat(i)
        if (i % 4) == 1:
            print "Beat"
        else:
            print "Beat / 4"
        sleep(beat)
        i += 1

def sendBeat(num):
    # sequencer.beat(num)
    print num

def one():
    global first, timeDeltas
    first = datetime.now()
    timeDeltas = []

def two():
    global second
    second = datetime.now()
    delta = second - first
    total = delta.seconds + (float(delta.microseconds) / 1000000)
    timeDeltas.append(total)

def three():
    global third
    third = datetime.now()
    delta = third - second
    total = delta.seconds + (float(delta.microseconds) / 1000000)
    timeDeltas.append(total)

def four():
    global fourth
    fourth = datetime.now()
    delta = fourth - third
    total = delta.seconds + (float(delta.microseconds) / 1000000)
    timeDeltas.append(total)
    startLoop()

grammar = Grammar("JamR")
grammar.add_rule(tempoOne())
grammar.add_rule(tempoTwo())
grammar.add_rule(tempoThree())
grammar.add_rule(tempoFour())
grammar.load()

while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)