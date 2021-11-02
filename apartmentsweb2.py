class Roommate:
    def __init__(self,name,days):
        self.name = name
        self.days = days

    def pay(self,mate_date,t):
        amount = (int(self.days) * t) / (mate_date + self.days)
        return amount

