from classes import *

def WriteToJSON(decks):
    f = open("data.json", "w")
    f.write(decks.to_json())
    f.close()