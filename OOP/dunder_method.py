class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)
    
    def __getitem__(self, index):
        return self._transactions[index]
    
    def __iter__(self):
        return iter(self._transactions)
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    
    def __add__(self, value):
        self._transactions.append(value)

    def __sub__(self, value):
        self._transactions.append(-value)

    
    def __str__(self):
        return f"{self.name} account - balance: {str(self.balance)}"
    



acc1 = Account('1', 1000)
acc1 + 30 
acc1 - 10000
print(acc1.balance)
acc2 = Account('2', 3000)

print(list(acc1))
print(acc1)
