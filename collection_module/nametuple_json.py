from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

blog_nt = namedtuple("blog", ["name", "founders", "started", "tags", "location", "site"])
def dict2nt(dict_):
    value_arr = []
    for i in dict_.items():
        value_arr.append(i[1])

    name, founders, started, tags, location, site = value_arr
    return blog_nt(name, founders, started, tags, location, site)

def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)
