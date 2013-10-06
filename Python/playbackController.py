# import sequencer
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

def setGenre(genre):
  print "something"
  # sequencer.setGenre(genre)

def setTempo(newTempo):
  global tempo
  tempo = newTempo
  # sequencer.setTempo(tempo)

def setProgression(newProgression):
  progression = newProgression
  # sequencer.setProgression

def setKey(newKey):
  key = newKey
  # sequencer.setKey(key)

def increaseTrack(track):
  trackVolume[track] += 1

def decreaseTrack(track):
  trackVolume[track] -= 1

def startLoop():
  global tempo
  Timer(tempo, loop).start()

def loop():
  global tempo
  print "beat"
  timer = Timer(tempo, loop).start()
  # sequencer.beat(i)

def stopLoop():
  loop = False

def sendBeat(num):
  # sequencer.beat(num)
  print num