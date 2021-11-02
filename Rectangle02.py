import random
class Rectangle:
    def point(self,player):
        self.x1=random.randint(1,19)
        self.x2=random.randint(self.x1+1,20)
        self.y1=random.randint(1,19)
        self.y2=random.randint(self.y1+1,20)
print("Rectangle x1-x2",Rectangle.x1,Rectangle.x2)
print("Rectangle y1-y2",Rectangle.y1,Rectangle.y2)


GuessX=int(input("Guess the x "))
GuessY=int(input("Guess the y "))

class player:
    def guessXY(self):
      self.guessX = GuessX
      self.guessY = GuessY
if player.guessX>=Rectangle.x1 and player.guessX <= Rectangle.x2 and player.guessY >= Rectangle.y1 and player.guessY <= Rectangle.y2:
    print("You win")
else :
    print("You Lose")

r = Rectangle()
pl = player()
pl.guessXY()
r.point(pl)