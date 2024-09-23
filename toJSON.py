from classes import *

def toJSON(decks):
    f = open("data.json", "w")
    f.write(decks.to_json())
    f.close()