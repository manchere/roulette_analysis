import sys
import config as conf
from qtpy import QtWidgets
from views.view import View
from dbconn import DbConnection


class Main(QtWidgets.QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        self.view = View()
        self.conn = DbConnection(conf.DB['db'], conf.DB['host'], conf.DB['user'], conf.DB['pass']).connect()


if __name__ == '__main__':
    main = Main(sys.argv)
    main.view.show()
    sys.exit(main.exec())
