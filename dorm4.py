
class Renter:
    def __init__(self,name):
        self.name = name
        self.day = 0
        
    def pay(self,dorm):
        occupants = dorm.occupants
        renter_no = len(occupants)
        i = 0
        s = 0
        while i < renter_no:
            s = s+occupants[i].day
            i = i+1
        p = dorm.rental_fee/s
        return(self.day*p)

class Dorm:
    def __init__(self):
        self.occupants = []
        self.rental_fee = 0

room = Dorm()

room.rental_fee = (int(input("Enter the total amount of rent : ")))
renter_no = int(input("Number of occupants : "))
d = input("What is the bill period? E.g. 22 Feb : ")

i = 0
while i < renter_no:
    renter = Renter(input("Renter no. "+str(i+1)+"'s Name : "))
    renter.day = (int(input(str(renter.name)+"'s day(s) of stay : ")))
    room.occupants.append(renter)
    i = i+1

print(d)

i = 0
while i < renter_no:
    renter = room.occupants[i]
    print(str(renter.name)+"'s rent : "+str(renter.pay(room)))
    i=i+1