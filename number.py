import json


class Number:

    def __init__(self, number):
        with open('color_scheme.json', 'r') as f:
            color_data = json.load(f)
        self.number = number
        self.color = color_data[str(number)]
        self.rank = None

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, value):
        self.number = value

    @property
    def color(self):
        return self.color

    @property
    def rank(self):
        return self.rank

    @rank.setter
    def rank(self, value):
        self.rank = value


