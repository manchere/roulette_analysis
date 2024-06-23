from qtpy import QtWidgets, QtCore, QtGui


class View(QtWidgets.QMainWindow):
    def __init__(self):
        super(View, self).__init__()

        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.window)
        self.setCentralWidget(self.window)
        self.txt_number = QtWidgets.QLineEdit()

        self.lst_output = QtWidgets.QListWidget()

        self.layout.addWidget(self.txt_number)
        self.layout.addWidget(self.lst_output)

        self.lst_output.setAlternatingRowColors(True)
        self.lst_output.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove
        )

        self.txt_number.returnPressed.connect(self.add_number)

    def add_number(self):
        self.lst_output.addItem(self.txt_number.text())


