import re

from qtpy import QtWidgets

from tool import _validate_field
from utilities import NumberLabel
from views.analysis import get_n_most_frequent, get_n_least_frequent, get_diff_of_arr

from number import Number


class View(QtWidgets.QMainWindow):
    def __init__(self):
        super(View, self).__init__()

        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.window)
        self.setCentralWidget(self.window)
        self.txt_number = QtWidgets.QLineEdit()
        self.lst_output = QtWidgets.QListWidget()
        self.temp = TemperatureLayout()

        self.layout.addLayout(self.temp)
        self.layout.addWidget(self.txt_number)
        self.layout.addWidget(self.lst_output)

        self.lst_output.setAlternatingRowColors(True)
        self.lst_output.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove
        )
        _validate_field(self.txt_number)
        self.txt_number.returnPressed.connect(self.add_number)

    def add_number(self):
        self.lst_output.insertItem(0, self.txt_number.text())
        most_freq = get_n_most_frequent(self.get_QListItems(), 5, rate=False)
        least_freq = get_diff_of_arr(
            set(get_n_least_frequent(self.get_QListItems(), 5, rate=False)),
            set(most_freq)
        )
        self.temp.fill_temperature_bar(self.temp.hot_labels, most_freq, self.get_QlistCount())
        self.temp.fill_temperature_bar(self.temp.cold_labels, least_freq, self.get_QlistCount())

    def get_QListItems(self):
        return [self.lst_output.item(x).text() for x in range(self.lst_output.count())]

    def get_QlistCount(self):
        return len(self.get_QListItems())


class TemperatureLayout(QtWidgets.QHBoxLayout):

    def __init__(self):
        super(TemperatureLayout, self).__init__()

        self.main_hot_layout = QtWidgets.QVBoxLayout()
        self.main_cold_layout = QtWidgets.QVBoxLayout()
        self.hot_bar_layout = QtWidgets.QHBoxLayout()
        self.cold_bar_layout = QtWidgets.QHBoxLayout()

        self.addLayout(self.main_hot_layout)
        self.addLayout(self.main_cold_layout)

        self.main_hot_layout.addWidget(QtWidgets.QLabel("Hot Numbers"))
        self.main_hot_layout.addLayout(self.hot_bar_layout)
        self.main_cold_layout.addWidget(QtWidgets.QLabel("Cold Numbers"))
        self.main_cold_layout.addLayout(self.cold_bar_layout)

        self.hot_labels = []
        self.cold_labels = []

        self.create_temp_widget()

    def create_temp_widget(self):
        for i in range(5):
            self.hot_labels.append(QtWidgets.QLabel())
            self.cold_labels.append(QtWidgets.QLabel())
            self.hot_bar_layout.addWidget(self.hot_labels[-1])
            self.cold_bar_layout.addWidget(self.cold_labels[-1])

    def fill_temperature_bar(self, labels, list_set, rank=0):
        for pos, data in enumerate(list_set):
            labels[pos].setText(str(data))
            num = Number(data)
            labels[pos].setStyleSheet(f"background-color : {num.color};"
                                      f"color : white ")

    def manage_number(self, number, rank):
        num = Number(number)
        num.rank = rank




