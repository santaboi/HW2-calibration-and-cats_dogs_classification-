from PyQt5 import QtCore, QtGui, QtWidgets

import sys

import MainWindow as ui
from Q1.Q1 import Question1
# from Q2.Q2 import Question2
from Q3.Q3 import Question3
from Q4.Q4 import Question4

class Main(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Question 1
        self.pushButtonDrawContour.clicked.connect(Q1Object.drawContour)
        self.pushButtonCountRings.clicked.connect(lambda: Q1Object.showNumberOfRings(self.labelRings1, self.labelRings2))

        # Question 2
        # self.pushButtonDetectCorners.clicked.connect(Q2Object.btn_findCorner)
        # self.pushButtonFindIntrinsicMatrix.clicked.connect(Q2Object.btn_findIntrinsic)
        # self.pushButtonFindExtrinsicMatrix.clicked.connect(lambda: Q2Object.btn_findExtrinsic(self.textEditExtrinsicMatrixImage.toPlainText()))
        # self.pushButtonFindDistortionMatrix.clicked.connect(Q2Object.btn_findDistortion)
        # self.pushButtonShowUndistortedResult.clicked.connect(Q2Object.btn_showUndistortion)

        # Question 3
        self.pushButtonShowWordsOnBoard.clicked.connect(lambda: Q3Object.onBoard(self.textEditWords.toPlainText()))
        self.pushButtonShowWordsVertically.clicked.connect(lambda: Q3Object.Vertical(self.textEditWords.toPlainText()))

        # Question 4
        self.pushButtonShowDisparityMap.clicked.connect(Q4Object.stereoDisparityMap)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Q1Object = Question1()
    # Q2Object = Question2()
    Q3Object = Question3()
    Q4Object = Question4()
    window = Main()
    window.show()
    sys.exit(app.exec_())