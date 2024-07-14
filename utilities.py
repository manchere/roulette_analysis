from qtpy import QtGui, QtWidgets


class NumericValidator(QtGui.QValidator):
    def validate(self, input_str, pos):
        if input_str.isnumeric() or input_str == "":
            return QtGui.QValidator.Acceptable, input_str, pos
        else:
            return QtGui.QValidator.Invalid, input_str, pos


class NumberLabel(QtWidgets.QLabel):

    def mousePressEvent(self, ev):
        pass
