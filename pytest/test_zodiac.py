from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

# from pytest.test_zodiac import (get_signs, get_sign_with_most_famous_people,
#                     signs_are_mutually_compatible, get_sign_by_date)

from zodiac import Sign, get_signs, get_sign_with_most_famous_people, signs_are_mutually_compatible, get_sign_by_date

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)

# write your pytest code here ...

def test_get_signs(signs):
    assert len(signs) == 12
    assert signs[0].name == 'Aries'
    assert signs[0].compatibility == ["Leo","Sagittarius","Gemini","Aquarius"]

def test_get_sign_with_most_famous_people(signs):
    assert get_sign_with_most_famous_people(signs) == ("Scorpio", 35)

def test_signs_are_mutually_compatible(signs):
    assert signs_are_mutually_compatible(signs, "Virgo", "Aries") == False
    assert signs_are_mutually_compatible(signs, "Aries", "Leo") == True


def test_get_sign_by_date(signs):
    assert get_sign_by_date(signs, datetime(2026, 3, 21)) == "Aries"