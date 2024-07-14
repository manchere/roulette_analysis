import re

from qtpy import QtWidgets

from tool import _validate_field
from utilities import NumberLabel
from views.analysis import get_n_most_frequent

from number import Number


class View(QtWidgets.QMainWindow):
    def __init__(self):
        super(View, self).__init__()

        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.window)
        self.setCentralWidget(self.window)
        self.txt_number = QtWidgets.QLineEdit()
        self.lst_output = QtWidgets.QListWidget()
        self.hot_labels = []

        self.temp_bar_layout = QtWidgets.QHBoxLayout()
        self.hot_bar_layout = QtWidgets.QHBoxLayout()
        self.cold_bar_layout = QtWidgets.QHBoxLayout()

        self.layout.addLayout(self.temp_bar_layout)
        self.layout.addWidget(self.txt_number)
        self.layout.addWidget(self.lst_output)

        self.lst_output.setAlternatingRowColors(True)
        self.lst_output.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove
        )

        _validate_field(self.txt_number)
        self.txt_number.returnPressed.connect(self.add_number)

        self.temp_bar_layout.addLayout(self.hot_bar_layout)
        self.temp_bar_layout.addLayout(self.cold_bar_layout)

        self.create_temp_widget()

    def add_number(self):
        self.lst_output.insertItem(0, self.txt_number.text())
        self.fill_temperature_bar()

    def fill_temperature_bar(self):
        for pos, data in enumerate(get_n_most_frequent(self.get_QListItems(), 5)):
            self.hot_labels[pos].setText(str(data[0]))

    def get_QListItems(self):
        print(self.lst_output.item(0).text())
        return [self.lst_output.item(x).text() for x in range(self.lst_output.count())]

    def create_temp_widget(self):
        for i in range(5):
            self.hot_labels.append(QtWidgets.QLabel())
            self.hot_bar_layout.addWidget(self.hot_labels[-1])


