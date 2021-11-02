import random
class Deck:
    def __init__(self):
        self.deckall=[]
        dok = ["♣","♠","♥","♦"]
        number =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for type in dok :
            for num in number :
                self.__init__.append(dok[type]+number[num])
class Player:
    def __init__(self):
        self.hand=[]
        
    def draw(self):
