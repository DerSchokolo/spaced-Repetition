from classes import *
from getFromJSON import getFromJSON
from toJSON import toJSON

decks = getFromJSON()

decks.decks[1].learnDeck()

toJSON(decks)