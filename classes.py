import datetime

GlobalIdCard = 0
class Card:
    def __init__(self, front, back):
        global GlobalIdCard
        self.id = GlobalIdCard
        GlobalIdCard = GlobalIdCard + 1

        self.date = datetime.datetime.now().date()

        self.front = front
        self.back = back

    def __str__(self):
        return "ID: " + str(self.id) + " DATE: " + str(self.date) + " FRONT: " + self.front + " BACK: " + self.back

GlobalIDDeck = 0
class Deck:
    def __init__(self, Name):
        global GlobalIDDeck
        self.id = GlobalIDDeck
        GlobalIDDeck = GlobalIDDeck + 1
        self.cards = []

        self.Name = Name

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        return "ID: " + str(self.id) + " NAME: " + self.Name + " CARDS: " + str(self.cards)