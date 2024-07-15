import json


class Number:

    def __init__(self, number):
        with open('color_scheme.json', 'r') as f:
            color_data = json.load(f)
        self._number = number
        self._color = color_data[str(number)]
        self._rank = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def color(self):
        return self._color

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value


class Game:
    pass

class Bet:
    pass