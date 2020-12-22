class Currency():

    def __init__(self, coin, value):
        self.coin = coin
        self.value = value

    def __str__(self):
        return f'{self.value} {self.coin}'

    def __int__(self):
        return self.value

    def __repr__(self):
        return f'{self.value} {self.coin}'

    def __add__(self, other):

        if type(other) == type(self.value):
            return self.value + other
        if self.coin == other.coin:
            self.value += other.value
            return self.value
        
        return f'Cannot add between Currency type <{self.coin}> and <{other.coin}>'
    
    def __iadd__(self, other):

        if type(other) == type(self.value):
            return self.value + other
        if self.coin == other.coin:
            self.value += other.value
            return self.value
        
        return f'Cannot add between Currency type <{self.coin}> and <{other.coin}>'

  

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)
print(c1.__str__())
print(c1.__int__())
print(c1.__repr__())
print(c1 + 5)
print(c1 + c2)
print(c1)
print(c1 + c3)
c1 += 5
print(c1)
