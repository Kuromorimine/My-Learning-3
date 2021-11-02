class Bill:
    def __init__(self,amount):
        self.amount=amount
        
class Roommate:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    def pay(self,bill,roommate):
        weight = self.days/self.days+roommate.days
        to_pay = bill.amount + weight
        return to_pay
    