
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import fast_article

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = fast_article.MainWin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
