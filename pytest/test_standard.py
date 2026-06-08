from unittest.mock import patch
import pytest
import color
import re


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    for _ in range(10):
        color = next(gen)
        assert isinstance(color, str)
        assert color.startswith("#")
        assert len(color) == 7
        assert re.fullmatch(r'[0-9A-F]{6}', color[1:]) is not None

 