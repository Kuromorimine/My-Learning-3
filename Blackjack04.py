import random

class Deck:
    def __init__(self):#สร้างไพ่
        self.deckall=[]
        self.deckshuffled=[]
        dok = ["♣","♠","♥","♦"]
        number =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for type in dok :
            for num in number :
                self.deckall.append(dok[type]+number[num])

    def shuffle(self):
        deckshuffle=Deck.deckall
        for shuff in range(53):
            z=random.randint(1,53)
            self.deckshuffled.append(deckshuffle[z])
            self.deckshuffled.remove(deckshuffle[z])
        #สับไพ่
    

class Player:
    def __init__(self):
        self.hand=[]
        self.deck=[Deck.deckshuffled]
    def draw(self):
        i=0
        while i<2:
            self.hand.append(str(Deck.deckshuffled[i]))
            self.deck.remove(str(Deck.deckshuffled[i]))
            i=i+1
        
        #จั่วขึ้นมือจากด้านบน
        #showcard
    def show(self):
        print(str(self.hand))

class Dealer(Player):
    def __init__(self):
        self.hand=[]
    def show_one():
        print(str(Dealer.hand))
    def count(self):
        countnum=0
        for num in range(2):
            if self.hand[num][1] == "A":
                countnum = countnum + 1
            if self.hand[num][1] == "2":
                countnum = countnum + 2
            if self.hand[num][1] == "3":
                countnum = countnum + 3
            if self.hand[num][1] == "4":
                countnum = countnum + 4
            if self.hand[num][1] == "5":
                countnum = countnum + 5
            if self.hand[num][1] == "6":
                countnum = countnum + 6
            if self.hand[num][1] == "7":
                countnum = countnum + 7
            if self.hand[num][1] == "8":
                countnum = countnum + 8
            if self.hand[num][1] == "9":
                countnum = countnum + 9
            if self.hand[num][1] == "1" or self.hand[num][1] == "J" or self.hand[num][1] == "Q" or self.hand[num][1] == "K":
                countnum = countnum + 10

        if countnum <= 21:
            pass
        else:
            print("Game Over")
            
        #เช็คแต้ม รวมแต้ม

class Blackjack():
    def __init__(self):
        pass
    def 



print("Black_Jack")
i
