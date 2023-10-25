from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import random as  rd

password_len = 0

charSet = []
specialChars = ['@','#','$','&','&','*','*','(','(']

passwordGeneratedString = ""
passwordGenerated = []

for char in range(ord('a'), ord('z') + 1):
    charSet.append(chr(char))
    charSet.append(chr(char).upper())    


class Ui_MainWindow(object):
    
    def getSpinNumber(self):
        self.textEdit.clear()
        password_len = self.spinBox.value()
        passwordGenerated = []
        for random in range(0,password_len+1):
            randomChar = rd.choice(charSet)
            randomSpecialChar = rd.choice(specialChars)
            passwordGenerated.append(randomChar)
            passwordGenerated.append(randomSpecialChar)
        passwordGeneratedString=''.join(passwordGenerated)
        self.textEdit.setText(passwordGeneratedString)
    
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 462)
        icon = QtGui.QIcon.fromTheme("applications-graphics")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a SpinBox for selecting password length
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(50)
        self.spinBox.setObjectName("spinBox")
        
        # Create a TextEdit widget for displaying generated password
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 360, 721, 70))
        
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        # Create a CommandLinkButton for generating the password
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(660, 190, 111, 41))
        self.commandLinkButton.clicked.connect(self.getSpinNumber)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setMouseTracking(False)
        icon = QtGui.QIcon.fromTheme("computer")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        # Create labels for various UI elements
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 120, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(45)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 330, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum O")
        font.setPointSize(16)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 330, 21, 18))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        
        # Set the central widget for the main window
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Create a status bar for the main window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect UI elements to translations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Gen"))
        self.commandLinkButton.setText(_translate("MainWindow", "GENERATE"))
        self.label.setText(_translate("MainWindow", "Select Length Of Desired Password"))
        self.label_2.setText(_translate("MainWindow", "Password Generator"))
        self.label_3.setText(_translate("MainWindow", "GENERATED PASSWORD"))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())