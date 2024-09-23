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

    def showCard(self):
        print(self.front)
        input("Press Enter to show back...")
        print(self.back)
        answer = input("Did you know the card? (yes/no)" )
        if answer == "yes":
            self.date = (datetime.datetime.now() + datetime.timedelta(days=5)).date()
            print("Nice Work! you will see this card again: " + str(self.date))
        elif answer == "no":
            self.date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
            print("Better luck next time! you will see this card again: " + str(self.date))
        else:
            print("ERROR")


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

    def learnDeck(self):
        date = datetime.datetime.now().date()
        for card in self.cards:
            if card.date == date:
                card.showCard()