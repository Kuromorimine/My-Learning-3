class Dorm():
    def __init__(self) -> None:
        self.ppl=[]
        self.rent=int(input('fee: '))
        self.ppl.append(int(input('person1 day lived: ')))
        self.ppl.append(int(input('person2 day lived: ')))
        self.calcu()
    
    def calcu(self):
        print('person1 fee: ',self.ppl[0]*self.rent/sum(self.ppl))
        print('person2 fee: ',self.ppl[1]*self.rent/sum(self.ppl))

a=Dorm()