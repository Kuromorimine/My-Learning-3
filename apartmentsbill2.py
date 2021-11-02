from apartmentsweb2 import Roommate

total = int(input("Enter the total amount: "))
bill = input("What is the bill period? E.g. Oct 12: ")

name1 = input("What is your name? ")
days1 = int(input(f"How many days did {name1} stay? "))

name2 = input("What is yout roommate name? ")
days2 = int(input(f"How many days did {name2} stay? "))

person1 = Roommate(name1,days1,total)
person2 = Roommate(name2,days2,total)