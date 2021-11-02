class Complex:
    #constructor
    def _init_(self,real,imaginary):
        self.r=real
        self.i=imaginary
x=Complex(3.0,-4.5)#instantiate
print(x.r, x.i)