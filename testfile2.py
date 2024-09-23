from classes import *
from getFromJSON import getFromJSON
from testfile import decks
from toJSON import WriteToJSON

getFromJSON()

decks.decks[0].learnDeck()

WriteToJSON(decks)