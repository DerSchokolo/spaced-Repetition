from classes import *
from toJSON import WriteToJSON

decks = Decks()
decks.createDeck("Deck1")
decks.decks[0].createCard("front1", "back1")
decks.decks[0].createCard("front2", "back2")

decks.createDeck("Deck2")
decks.decks[1].createCard("front1", "back1")
decks.decks[1].createCard("front2", "back2")

print(decks)

WriteToJSON(decks)