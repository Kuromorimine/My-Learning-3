class Roommate():
    def __init__(self,name,days):
        self.name = name
        self.days = days
    
    def pay(self,totalbill):
        amount=(self.days * totalbill) / (person1_day+person2_day)
        return amount
totalbill=int(input("total bill : "))

person1_name=input("Person 1 name ? : ")
person1_day=int(input(str(person1_name)+" stay ? : "))

person2_name=input("Person 2 name ? : ")
person2_day=int(input(str(person2_name)+" stay ? : "))

person1=Roommate(person1_name,person1_day)
person2=Roommate(person2_name,person2_day)

print(person1_name,"pays : ",person1.pay(totalbill))
print(person2_name,"pays : ",person2.pay(totalbill))
