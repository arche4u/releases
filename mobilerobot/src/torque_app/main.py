import sys
from include.amrtorque import *


class main_class(MobileRobotTroque):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = main_class()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
