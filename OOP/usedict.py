from collections import UserDict
from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(UserDict):
    """
    Override UserDict to print a message every time a new person is added
    that has the same birthday (day+month) as somebody already in the dict
    """

    def __setitem__(self, key, value):
        # Your logic here
        for name, bday in self.data.items():
            if (bday.month, bday.day) == (value.month, value.day):
                print(MSG.format(key))
                break
        super().__setitem__(key, value)
        



bd = BirthdayDict()
bd['bob'] = date(1995,3,15)
bd['bib'] = date(1995,4,15)
bd['same'] = date(1995,3,15)
