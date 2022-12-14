# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUITicTacToe.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]

playFlag = 0
playerX = 0
playerO = 0
winner = ''
mark = ''

class Ui_Form(object):
    def resetBoard(self) -> None:
        """
        Resets board function
        :param self:
        :return:
        """
        global playFlag, placement
        playFlag = 0
        placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.pa1.setEnabled(True)
        self.pa2.setEnabled(True)
        self.pa3.setEnabled(True)
        self.pa4.setEnabled(True)
        self.pa5.setEnabled(True)
        self.pa6.setEnabled(True)
        self.pa7.setEnabled(True)
        self.pa8.setEnabled(True)
        self.pa9.setEnabled(True)

        self.pa1.setText('')
        self.pa2.setText('')
        self.pa3.setText('')
        self.pa4.setText('')
        self.pa5.setText('')
        self.pa6.setText('')
        self.pa7.setText('')
        self.pa8.setText('')
        self.pa9.setText('')


    def bot(self) -> None:
        """
        Function so rival bot chooses a tile
        :param self:
        :return:
        """
        global playFlag
        mark = 'O'
        pos = 0
        if placement:
            pos = random.choice(placement)
        if pos == 1:
            self.pa1.setText(mark)
            self.pa1.setEnabled(False)
            placement.remove(pos)

        if pos == 2:
            self.pa2.setText(mark)
            self.pa2.setEnabled(False)
            placement.remove(pos)
        if pos == 3:
            self.pa3.setText(mark)
            self.pa3.setEnabled(False)
            placement.remove(pos)
        if pos == 4:
            self.pa4.setText(mark)
            self.pa4.setEnabled(False)
            placement.remove(pos)
        if pos == 5:
            self.pa5.setText(mark)
            self.pa5.setEnabled(False)
            placement.remove(pos)
        if pos == 6:
            self.pa6.setText(mark)
            self.pa6.setEnabled(False)
            placement.remove(pos)
        if pos == 7:
            self.pa7.setText(mark)
            self.pa7.setEnabled(False)
            placement.remove(pos)
        if pos == 8:
            self.pa8.setText(mark)
            self.pa8.setEnabled(False)
            placement.remove(pos)
        if pos == 9:
            self.pa9.setText(mark)
            self.pa9.setEnabled(False)
            placement.remove(pos)
        playFlag += 1

    def btnClk(self, pos: int) -> None:
        """
        Register what tile the user clicks
        :param self:
        :param pos: Holds position of tile
        :type pos: int
        :return:
        """
        global playFlag, mark
        mark = 'X'


        if pos == 1:
            self.pa1.setText(mark)
            self.pa1.setEnabled(False)
            placement.remove(pos)

        if pos == 2:
            self.pa2.setText(mark)
            self.pa2.setEnabled(False)
            placement.remove(pos)
        if pos == 3:
            self.pa3.setText(mark)
            self.pa3.setEnabled(False)
            placement.remove(pos)
        if pos == 4:
            self.pa4.setText(mark)
            self.pa4.setEnabled(False)
            placement.remove(pos)
        if pos == 5:
            self.pa5.setText(mark)
            self.pa5.setEnabled(False)
            placement.remove(pos)
        if pos == 6:
            self.pa6.setText(mark)
            self.pa6.setEnabled(False)
            placement.remove(pos)
        if pos == 7:
            self.pa7.setText(mark)
            self.pa7.setEnabled(False)
            placement.remove(pos)
        if pos == 8:
            self.pa8.setText(mark)
            self.pa8.setEnabled(False)
            placement.remove(pos)
        if pos == 9:
            self.pa9.setText(mark)
            self.pa9.setEnabled(False)
            placement.remove(pos)

        playFlag += 1
        self.bot()
        self.chkWin()






    def chkWin(self) -> None:
        """
        Checks to see if either player has won
        :param self:
        :return:
        """
        global playerX, playerO, winner, placement
        winner = ''

        if self.pa1.text() == self.pa2.text() and self.pa2.text() == self.pa3.text():
            winner = self.pa1.text()
        elif self.pa4.text() == self.pa5.text() and self.pa5.text() == self.pa6.text():
            winner = self.pa4.text()
        elif self.pa7.text() == self.pa8.text() and self.pa8.text() == self.pa9.text():
            winner = self.pa7.text()
        elif self.pa1.text() == self.pa4.text() and self.pa4.text() == self.pa7.text():
            winner = self.pa1.text()
        elif self.pa2.text() == self.pa5.text() and self.pa5.text() == self.pa8.text():
            winner = self.pa2.text()
        elif self.pa3.text() == self.pa6.text() and self.pa6.text() == self.pa9.text():
            winner = self.pa3.text()
        elif self.pa1.text() == self.pa5.text() and self.pa5.text() == self.pa9.text():
            winner = self.pa1.text()
        elif self.pa3.text() == self.pa5.text() and self.pa5.text() == self.pa7.text():
            winner = self.pa3.text()
        elif not placement:
            winner = 'none'
        if winner == 'X':
            playerX += 1
            self.Result1.setText('Player X: '+str(playerX))
            self.resetBoard()
            placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if winner == 'O':
            playerO += 1
            self.Result2.setText('Player O: '+str(playerO))
            self.resetBoard()
            placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if winner == 'none':
            self.resetBoard()
            placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]



    def setupUi(self, Form: str) -> None:
        """
        Designer layout
        :param self:
        :param Form:
        :type Form: str
        :return:
        """
        Form.setObjectName("Form")
        Form.resize(365, 449)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 343, 348))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pa4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa4.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa4.setFont(font)
        self.pa4.setText("")
        self.pa4.setObjectName("pa4")
        self.gridLayout.addWidget(self.pa4, 1, 0, 1, 1)
        self.pa8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa8.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa8.setFont(font)
        self.pa8.setText("")
        self.pa8.setObjectName("pa8")
        self.gridLayout.addWidget(self.pa8, 2, 1, 1, 1)
        self.pa6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa6.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa6.setFont(font)
        self.pa6.setText("")
        self.pa6.setObjectName("pa6")
        self.gridLayout.addWidget(self.pa6, 1, 2, 1, 1)
        self.pa2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa2.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa2.setFont(font)
        self.pa2.setText("")
        self.pa2.setObjectName("pa2")
        self.gridLayout.addWidget(self.pa2, 0, 1, 1, 1)
        self.pa5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa5.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa5.setFont(font)
        self.pa5.setText("")
        self.pa5.setObjectName("pa5")
        self.gridLayout.addWidget(self.pa5, 1, 1, 1, 1)
        self.pa3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa3.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa3.setFont(font)
        self.pa3.setText("")
        self.pa3.setObjectName("pa3")
        self.gridLayout.addWidget(self.pa3, 0, 2, 1, 1)
        self.pa7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa7.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa7.setFont(font)
        self.pa7.setText("")
        self.pa7.setObjectName("pa7")
        self.gridLayout.addWidget(self.pa7, 2, 0, 1, 1)
        self.pa1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa1.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa1.setFont(font)
        self.pa1.setText("")
        self.pa1.setObjectName("pa1")
        self.gridLayout.addWidget(self.pa1, 0, 0, 1, 1)
        self.pa9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pa9.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pa9.setFont(font)
        self.pa9.setText("")
        self.pa9.setObjectName("pa9")
        self.gridLayout.addWidget(self.pa9, 2, 2, 1, 1)
        self.Result1 = QtWidgets.QLabel(Form)
        self.Result1.setGeometry(QtCore.QRect(10, 370, 111, 71))
        self.Result1.setObjectName("Result1")
        self.Result2 = QtWidgets.QLabel(Form)
        self.Result2.setGeometry(QtCore.QRect(230, 370, 111, 71))
        self.Result2.setObjectName("Result2")

        #reset button
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setGeometry(QtCore.QRect(120, 360, 101, 93))
        self.resetButton.setMinimumSize(QtCore.QSize(93, 93))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetBoard)


        #connects button to function
        self.pa1.clicked.connect(lambda: self.btnClk(1))
        self.pa2.clicked.connect(lambda: self.btnClk(2))
        self.pa3.clicked.connect(lambda: self.btnClk(3))
        self.pa4.clicked.connect(lambda: self.btnClk(4))
        self.pa5.clicked.connect(lambda: self.btnClk(5))
        self.pa6.clicked.connect(lambda: self.btnClk(6))
        self.pa7.clicked.connect(lambda: self.btnClk(7))
        self.pa8.clicked.connect(lambda: self.btnClk(8))
        self.pa9.clicked.connect(lambda: self.btnClk(9))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form: str) -> None:
        """
        :param self:
        :param Form:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Result1.setText(_translate("Form", "Player X : 0"))
        self.Result2.setText(_translate("Form", "Player O : 0"))
        self.resetButton.setText(_translate("Form", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
