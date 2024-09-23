import datetime
import json

GlobalIdCard = 0
GlobalIDDeck = 0  # Initialize the global deck ID counter

class Card:
    def __init__(self, id, date, front, back):
        self.id = id
        self.date = date
        self.front = front
        self.back = back

    def __str__(self):
        return f"ID: {self.id} DATE: {self.date} FRONT: {self.front} BACK: {self.back}"

    def showCard(self):
        print(self.front)
        input("Press Enter to show back...")
        print(self.back)
        answer = input("Did you know the card? (yes/no)" )
        if answer == "yes":
            self.date = (datetime.datetime.now() + datetime.timedelta(days=5)).date()
            print("Nice Work! You will see this card again: " + str(self.date))
        elif answer == "no":
            self.date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
            print("Better luck next time! You will see this card again: " + str(self.date))
        else:
            print("ERROR")

    def to_dict(self):
        return {
            'id': self.id,
            'date': str(self.date),
            'front': self.front,
            'back': self.back
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

class Deck:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def createCard(self, front, back):
        global GlobalIdCard
        card = Card(GlobalIdCard, datetime.datetime.now().date(), front, back)
        self.addCard(card)
        GlobalIdCard += 1

    def __str__(self):
        return f"ID: {self.id} NAME: {self.name} CARDS: {len(self.cards)}"

    def learnDeck(self):
        date = datetime.datetime.now().date()
        for card in self.cards:
            if card.date == date:
                card.showCard()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cards': [card.to_dict() for card in self.cards]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

class Decks:
    def __init__(self):
        self.decks = []

    def addDeck(self, deck):
        self.decks.append(deck)

    def createDeck(self, name):
        global GlobalIDDeck
        deck = Deck(GlobalIDDeck, name)
        self.addDeck(deck)
        GlobalIDDeck += 1

    def to_dict(self):
        return {
            'decks': [deck.to_dict() for deck in self.decks]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return f"Decks: {len(self.decks)}"