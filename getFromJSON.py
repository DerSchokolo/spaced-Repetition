from classes import *
import json

def getFromJSON():
    f = open("data.json", "r")
    data_list = f.read()
    f.close()

    data_list = json.loads(data_list)
    decks = Decks()

    # Iterate over each deck in the JSON data
    for deck_data in data_list['decks']:
        # Create a new deck and add it to the decks collection
        decks.createDeck(deck_data['name'])
        current_deck = decks.decks[-1]  # Get the last added deck (which is the current one)

        # Iterate over the cards in the current deck
        for card_data in deck_data['cards']:
            # Create and add a new card to the current deck
            card = Card(card_data['id'], card_data['date'], card_data['front'], card_data['back'])
            current_deck.addCard(card)