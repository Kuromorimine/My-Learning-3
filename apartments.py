class Dorm:
    def __init__(self):
        self.allbill=int(input("All-Bill : "))
    def calculate(self,detail):
        permonth=int(detail.pay1)+int(detail.pay2) 
        print(int(detail.pay1)/int(permonth)*self.allbill)
        print(int(detail.pay2)/int(permonth)*self.allbill)
        #enter bill 
        #calculate bill
    
class People:
    def __init__(self):
        self.name1=input("Roommate 1 : ")
        self.name2=input("Roommate 2 : ")
        self.pay1 =int(input(self.name1+" Day ? : "))
        self.pay2 =int(input(self.name2+" Day ? : "))

detail=People()

bill=Dorm()

bill.calculate(detail)