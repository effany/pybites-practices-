from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    'Transaction',
    'giver points date',
    defaults=(None, None, datetime.now()))


class User:
    def __init__(self, name):
        self.name = name
        self._transactions = []

    @property
    def points(self):
        return [t.points for t in self._transactions]
    
    @property
    def karma(self):
        return sum(t.points for t in self._transactions)
    
    @property
    def fans(self):
        return len({t.giver for t in self._transactions if t.giver})
    
    def __add__(self, new_trasaction):
        self._transactions.append(new_trasaction)
        return self 
    
    def __str__(self):
        fan_word = 'fan' if self.fans == 1 else 'fans'
        return f"{self.name} has a karma of {self.karma} and {self.fans} {fan_word}"


transactions =  [
        Transaction(giver='alice', points=1),
        Transaction(giver='bob', points=2),
        Transaction(giver='tim', points=3),
        Transaction(giver='tim', points=4),
        Transaction(giver='alice', points=2),
    ]    

bob = User('bob')
alice = User('alice')
tim = User('tim')

bob + transactions[0]
alice + transactions[1]
bob + transactions[2]
alice + transactions[3]
tim + transactions[4]

print(alice.fans)
print(str(tim))