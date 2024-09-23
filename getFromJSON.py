from classes import *
import json

f = open("data.json", "r")
data_list = f.read()
f.close()

data_list = json.loads(data_list)

deck = Deck(data_list['id'], data_list['name'])
cards = data_list['cards']
for card in cards:
    deck.addCard(card = Card(card['id'], card['date'], card['front'], card['back']))

print(deck)