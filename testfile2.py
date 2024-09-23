from classes import *
from getFromJSON import getFromJSON
from testfile import decks
from toJSON import toJSON

getFromJSON()

decks.decks[0].learnDeck()

toJSON(decks)