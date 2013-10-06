import pygame
from pygame import midi

instrNums = {"kick": 1,
            "snare": 2,
            "hihat": 3}
genreNums = {"simple": 1,
              "blues": 2,
               "rock": 3,
         "electronic": 4}
rhythms = {}
key = 0 #a

pygame.init()
midi.init()
midi_out = midi.Output(12, 0) #port, channel

def setInstrument(name, value):
  filename = name + ".txt"
  with open(filename) as f:
    patterns = f.readlines()
    rhythms[name] = patterns[value]

def beat(index):
  sixteenth = index % 16
  for key in instruments:
    if rhythms[key][sixteenth] != 0:
      sendNote(key, rhythms[key][sixteenth])

def sendNote(name, value):
  instrNum = instrNums[name]
  midi_out.write_short(0x90, instrNum, value)

def setGenre(name):
  midi_out.write_short(0x90, 100, genreNums[name])

def setKey(letter):
  key = ord(letter) - ord('a')

def end():
  midi.quit()