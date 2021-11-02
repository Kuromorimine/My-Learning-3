class Roommate():
    def __init__(self,name,days):
        self.name = name
        self.days = int(days)
    
    def pay(self,total_amount):
        amount = int((self.days/(int(person1.days+person2.days)))*int(total_amount))
        return amount

total_amount = input("Enter the total amount: ")
bill_peroid = input("What is the bill period? E.g. June 25: ")
person1 = Roommate(input("What is your name? "),input("How many days did you stay? "))
person2 = Roommate(input("What is the name of the other roommate? "),input("How many days did he/she stay? "))
print(person1.name,"pays:",person1.pay(total_amount))
print(person2.name,"pays:",person2.pay(total_amount))
