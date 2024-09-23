from classes import *

Deck1 = Deck(0,"Deck1")

card1 = Card("front1", "back1")
card2 = Card("front2", "back2")
card3 = Card("front3", "back3")

Deck1.addCard(card1)
Deck1.addCard(card2)
Deck1.addCard(card3)


f = open("data.json", "w")
f.write(Deck1.to_json())
f.close()