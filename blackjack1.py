Deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
import random
class Player:
   def __init__(self):
     self.card1 = Deck[random.randint(0,len(Deck)-1)]
     Deck.remove(self.card1)
     self.card2 = Deck[random.randint(0,len(Deck)-1)]
     Deck.remove(self.card2)
     self.card3 = 0
     self.card4 = 0
     self.card5 = 0
     self.A = 0
   
   def drawCard(self):
     print(self.card1,self.card2)
     for j in range(1,4):
        i = str(input("Hit or stay "))
        if i == "Hit":
          if j == 1:
            self.card3 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card3)
            print(self.card1,self.card2,self.card3)
          if j == 2:
            self.card4 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card4)
            print(self.card1,self.card2,self.card3,self.card4)
          if j == 3:
            self.card5 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card5)
            print(self.card1,self.card2,self.card3,self.card4,self.card5)  
        if i == "Stay":
          break

   def check(self):
     if self.card1 == "J" or self.card1 == "Q" or self.card1 == "K":
       self.card1 = 10
     if self.card2 == "J" or self.card2 == "Q" or self.card2 == "K":
       self.card2 = 10
     if self.card3 == "J" or self.card3 == "Q" or self.card3 == "K":
       self.card3 = 10
     if self.card4 == "J" or self.card4 == "Q" or self.card4 == "K":
       self.card4 = 10
     if self.card5 == "J" or self.card5 == "Q" or self.card5 == "K":
       self.card5 = 10
     if self.card1 == "A":
       i = int(input("1 or 11 "))
       self.card1 = i
     if self.card2 == "A":
       i = int(input("1 or 11 "))
       self.card2 = i
     if self.card3 == "A":
       i = int(input("1 or 11 "))
       self.card3 = i
     if self.card4 == "A":
       i = int(input("1 or 11 "))
       self.card4 = i
     if self.card5 == "A":
       i = int(input("1 or 11 "))
       self.card5 = i
     self.A = (int(self.card1)+int(self.card2)+int(self.card3)+int(self.card4)+int(self.card5))
     if self.A > 21:
       self.A = 0

class Dealer:
    def __init__(self):
     self.card1 = Deck[random.randint(0,len(Deck)-1)]
     Deck.remove(self.card1)
     self.card2 = Deck[random.randint(0,len(Deck)-1)]
     Deck.remove(self.card2)
     self.card3 = 0
     self.card4 = 0
     self.card5 = 0
     self.A = 0
    def drawCard(self):
     print(self.card1,self.card2)
     for j in range(1,4):
        i = str(input("Hit or stay "))
        if i == "Hit":
          if j == 1:
            self.card3 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card3)
            print(self.card1,self.card2,self.card3)
          if j == 2:
            self.card4 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card4)
            print(self.card1,self.card2,self.card3,self.card4)
          if j == 3:
            self.card5 = Deck[random.randint(0,len(Deck)-1)]
            Deck.remove(self.card5)
            print(self.card1,self.card2,self.card3,self.card4,self.card5)  
        if i == "Stay":
          break

    def check(self):
     if self.card1 == "J" or self.card1 == "Q" or self.card1 == "K":
       self.card1 = 10
     if self.card2 == "J" or self.card2 == "Q" or self.card2 == "K":
       self.card2 = 10
     if self.card3 == "J" or self.card3 == "Q" or self.card3 == "K":
       self.card3 = 10
     if self.card4 == "J" or self.card4 == "Q" or self.card4 == "K":
       self.card4 = 10
     if self.card5 == "J" or self.card5 == "Q" or self.card5 == "K":
       self.card5 = 10
     if self.card1 == "A":
       i = int(input("1 or 11 "))
       self.card1 = i
     if self.card2 == "A":
       i = int(input("1 or 11 "))
       self.card2 = i
     if self.card3 == "A":
       i = int(input("1 or 11 "))
       self.card3 = i
     if self.card4 == "A":
       i = int(input("1 or 11 "))
       self.card4 = i
     if self.card5 == "A":
       i = int(input("1 or 11 "))
       self.card5 = i
     self.A = (int(self.card1)+int(self.card2)+int(self.card3)+int(self.card4)+int(self.card5))
     if self.A > 21:
       self.A = 0
    
    def compareScore(self,player):
     print("Player: ",int(player.card1)+int(player.card2)+int(player.card3)+int(player.card4)+int(player.card5))
     print("Dealer: ",int(self.card1)+int(self.card2)+int(self.card3)+int(self.card4)+int(self.card5))
     if player.A > self.A:
       print("You win")
     if player.A < self.A:
       print("You lose")
     if player.A == self.A:
       print("Tie")
p = Player()
d = Dealer()
p.drawCard()
p.check()
d.drawCard()
d.check()
d.compareScore(p)
