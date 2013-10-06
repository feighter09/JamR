import sequencer
from threading import Timer

"""
Interfaces with sequencer to control 
drum machine
"""

loop = False
key = 'c'
trackVolume = {
                "kick": 0,
                "snare": 0,
                "hihat": 0
              }
timer = 0
tempo = 0.0
i = 0

def setGenre(genre):
  sequencer.setGenre(genre)

def setTempo(newTempo):
  global tempo
  tempo = newTempo
  sequencer.setTempo(newTempo)

def setProgression(newProgression):
  print "progression"
  # sequencer.setProgression

def setKey(newKey):
  sequencer.setKey(key)

def increaseTrack(track):
  trackVolume[track] += 1

def decreaseTrack(track):
  trackVolume[track] -= 1

def loop():
  global tempo, timer, i
  print "beat"
  timer = Timer(tempo, loop).start()
  sequencer.beat(i)
  i += 1

def stopLoop():
  global timer
  timer.cancel()