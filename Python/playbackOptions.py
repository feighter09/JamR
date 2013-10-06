from dragonfly.all import *
from dragonfly.all import Grammar
from time import *
from datetime import datetime
import pythoncom, time

class GenreRule(CompoundRule):
  spec = "Let's [play] [some] <genre>"
  extras = [Choice("genre", {
                            "rock": "rock",
                            "(blues | jazz)": "blues",
                            "electronic": "electronic"
                           }
                  )
           ]

  def _process_recognition(self, node, extras):
    # setGenre(extras["genre"])
    print "You got it! Playing some %s" % genre

class IncTrackRule(CompoundRule):

  spec = "(more | increase) <track>"
  extras = [Choice("track", {
                            "kick": "kick",
                            "snare": "snare",
                            "[high] hat": "high hat",
                            "cowbell": "cowbell"
                           }
                  )
           ]

  def _process_recognition(self, node, extras):
    print "You got it! More %s" % extras["track"]
    # moreTrack(extras["track"])

class DecTrackRule(CompoundRule):

  spec = "(less | decrease) <track>"
  extras = [Choice("track", {
                            "kick": "kick",
                            "snare": "snare",
                            "[high] hat": "high hat",
                            "cowbell": "cowbell"
                           }
                  )
           ]

  def _process_recognition(self, node, extras):
    print "You got it! Less %s" % extras["track"]
    # lessTrack(extras["track"])

class ChangeKeyRule(CompoundRule):

  spec = "[change [to]] key (to | of) <key>"
  extras = [Choice("key", {
                          "a": "a",
                          "b": "b",
                          "c": "c",
                          "d": "d",
                          "e": "e",
                          "f": "f",
                          "g": "g"
                         }
                  )
           ]

  def _process_recognition(self, node, extras):
    print "You got it! Changing to the key of %s" % extras["key"]
    # setKey(extras["key"])

grammar = Grammar("JamR")
grammar.add_rule(GenreRule())
grammar.add_rule(IncTrackRule())
grammar.add_rule(DecTrackRule())
grammar.add_rule(ChangeKeyRule())
grammar.load()

while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)
