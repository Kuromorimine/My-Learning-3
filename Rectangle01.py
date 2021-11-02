import random 
class Point:
    def points(self):
        self.x1=random.randint(1,20)
        self.x2=random.randint(1,20)
        self.y1=random.randint(1,10)
        self.y2=random.randint(1,10)
        print("x1 =",self.x1)
        print("x2 =",self.x2)
        print("x3 =",self.y1)
        print("x4 =",self.y2)

class Rectangle(Point):
    def answer(self):
        self.x=int(input("x = "))
        self.y=int(input("y = "))
    def check(self):
        if self.x1 < self.x < self.x2 and self.y1 < self.y < self.y2 :
            print("correct")
        else :
            print("not correct")

same =Point()
same.points()
obj1=Rectangle()
obj1.answer()
obj1.check()


            