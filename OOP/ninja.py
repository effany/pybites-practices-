from dataclasses import dataclass, field
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass(order=True)
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str = field(compare=False)
    bites: int = field(compare=True)
    

    def __str__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    rankings: list = field(default_factory=list)

    def __len__(self):
        return len(self.rankings)

    def add(self, ninja):
        return self.rankings.append(ninja)
    
    def dump(self):
        sort_ranks = sorted(self.rankings, key=lambda x: x.bites)
        if sort_ranks:
            self.rankings.remove(sort_ranks[0])
        return sort_ranks[0]
    
    def highest(self, counter=1):
        if counter > len(self.rankings):
            raise ValueError('counter is bigger then the number of ninjas')
        sort_ranks = sorted(self.rankings, key=lambda x: x.bites, reverse=True)
        return sort_ranks[0:counter]
    
    def lowest(self, counter=1):
        if counter > len(self.rankings):
            raise ValueError('counter is bigger then the number of ninjas')
        sort_ranks = sorted(self.rankings, key=lambda x: x.bites)
        return sort_ranks[0:counter]
    
    def pair_up(self, counter=3):
        high = self.highest(counter)
        low = self.lowest(counter)
        zip_array = zip(high, low)
        return list(zip_array)[:counter]


ninjas = zip(names, bites)
FIRST_NINJAS = [Ninja(*ninja) for ninja in zip(names, bites)]
#print(FIRST_NINJAS)
rankings = Rankings([])

for n in FIRST_NINJAS:
    rankings.add(n)

# print(rankings.highest())
# print(rankings.lowest())
print(rankings.pair_up(2))

# n1 = Ninja('snow', 283)
# n2 = Ninja('alex', 281)
# rankings = Rankings([])
# rankings.add(n1)
# rankings.add(n2)
# rankings.dump()
