class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)
    
    def __enter__(self):
        self._snapshot = self._transactions.copy()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if self.balance < 0:
            self._transactions = self._snapshot
        return False
    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager

