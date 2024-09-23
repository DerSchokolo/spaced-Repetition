from tkinter import *
from getFromJSON import getFromJSON

def StartAddDeckWindow():
    newWindow = Toplevel(root)
    newWindow.title("Add new Deck")
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()

def ModifyDeckWindow(deck):
    modDeckWindow = Toplevel(root)
    modDeckWindow.title("Modify Deck")
    modDeckWindow.geometry("400x400")
    Label(modDeckWindow, text =deck.name).grid(row=0, column=0, padx= 30, pady=20, sticky=W)

    for i in range(deck.NumberOfCards()):
        Label(modDeckWindow, text=deck.cards[i].id).grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
        Label(modDeckWindow, text=deck.cards[i].front).grid(row=i+1, column=1, padx=5, pady=5, sticky=W)
        Label(modDeckWindow, text=deck.cards[i].back).grid(row=i+1, column=2, padx=5, pady=5, sticky=W)

        Button(modDeckWindow, text='Modify Card', command=lambda i=i: ModifyCardWindow(deck.cards[i])).grid(row=i+1, column=3, padx=(0,0), sticky=W)

def ModifyCardWindow(card):
    modCardWindow = Toplevel(root)
    modCardWindow.title("Modify Card")
    modCardWindow.geometry("400x400")
    Label(modCardWindow, text =card.id).grid(row=0, column=0, padx= 30, pady=20, sticky=W)

    front = Entry(modCardWindow)
    back = Entry(modCardWindow)

    front.insert(0, card.front)
    back.insert(0, card.back)

    front.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    back.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    def saveEditCard():
        card.front = front.get()
        card.back = back.get()
        modCardWindow.destroy()

    Button(modCardWindow, text='Save', command=saveEditCard).grid(row=1, column=0, padx=(0,0), sticky=W)

# Create the main application window
root = Tk()
root.geometry("500x200")
root.title("Simple Tkinter App")

Label(root, text="Decks:").grid(row=0, column=0, padx= 30, pady=20, sticky=W)

decks = getFromJSON()

for i in range(decks.NumberofDecks()):
    Label(root, text=decks.decks[i].name).grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
    Button(root, text='Learn Deck', command=decks.decks[i].learnDeck).grid(row=i+1, column=1, padx=(0,0), sticky=W)
    Button(root, text='Modify Deck', command=lambda i=i: ModifyDeckWindow(decks.decks[i])).grid(row=i+1, column=2, padx=(0,0), sticky=W)

Button(root, text='Add Deck', command=StartAddDeckWindow).grid(row=0, column=1, padx=(0,0), sticky=W)

# Start the Tkinter event loop, which waits for user interactions
mainloop()