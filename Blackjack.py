import random
class Deck:
    def __init__(self):
        dok = ["♣","♠","♥","♦"]
        number =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range(4):
            for o in range(13):
                self.i,o=dok[i]+number[o]
                
