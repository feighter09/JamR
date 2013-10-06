import pygame
from pygame import midi

instrNums = {"kick": 1,
            "snare": 2,
            "hihat": 3,
            "crash": 4,
          "cowbell": 5}
genreNums = {"simple": 1,
              "blues": 2,
               "rock": 3,
         "electronic": 4}
keyNums = {
          "a": 0,
          "a#": 1,
          "b": 2,
          "c": 3,
          "c#": 4,
          "d": 5,
          "d#": 6,
          "e": 7,
          "f": 8,
          "f#": 9,
          "g": 10,
          "g#": 11
          }
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
  for key in rhythms:
    if rhythms[key][sixteenth] != '0':
      sendNote(key, rhythms[key][sixteenth])

def sendNote(name, value):
  instrNum = instrNums[name]
  midi_out.write_short(0x90, instrNum, value)

def setGenre(name):
  midi_out.write_short(0x90, 100, genreNums[name])

def setKey(note):
  midi_out.write_short(0x90, 101, keyNums[note])

def setTempo(tempo):
  midi_out.write_short(0x90, 102, int(float(60) / tempo))
def end():
  midi.quit()