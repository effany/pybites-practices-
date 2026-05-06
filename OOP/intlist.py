from collections import UserList
from statistics import mean, median
from decimal import Decimal


class IntList(UserList):
    """A specialized list that only allows integer values and provides mean/median properties."""

    def append(self, item):
        if not isinstance(item, (int, list, float, Decimal)):
            raise TypeError
        
        if isinstance(item, (int, float, Decimal)):
            super().append(item)
        else:
            for i in item:
                if not isinstance(i, (int, float, Decimal)):
                    raise TypeError
                super().append(i)

    @property
    def median(self):
        return median(float(x) for x in self)
    
    @property
    def mean(self):
        return mean(float(x) for x in self)
    
    def __add__(self, stuff):
        for i in stuff:
            if not isinstance(i, (int, float, Decimal)):
                raise TypeError
        return super().__add__(stuff)
    
    def __iadd__(self, other):
        for i in other:
            if not isinstance(i, (int, float, Decimal)):
                raise TypeError
        return super().__iadd__(other)


my_list = IntList([1,2,3])
my_list.append([5,6,7])
my_list += [3, 4]
print(my_list)