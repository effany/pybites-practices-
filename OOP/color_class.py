import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper())

    @staticmethod
    def hex2rgb(hex_value):
        new_hex_string = hex_value.replace("#", "")
        r = int(new_hex_string[0:2], 16)
        g = int(new_hex_string[2:4], 16)
        b = int(new_hex_string[4:6], 16)
        print(r,g,b)
        return (r,g,b)


    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        hex_string = ""
        
        if (not isinstance(rgb, (tuple, list))
            or len(rgb) != 3
            or not all(isinstance(i, int) and 0 <= i <=255 for i in rgb)):
            raise ValueError(f'Invalid RGB value: {rgb}')
        return '#' + ''.join(f"{i:02x}" for i in rgb)

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            return 'Unknown'
        return f'{self.rgb}'


color = Color('puke green')
print(color)
# print(color)
# color.hex2rgb('#000000')
# color.rgb2hex((255, 128, 0))