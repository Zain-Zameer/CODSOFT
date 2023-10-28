from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# List to store tasks and save them when printing them on text file
tasks = []

class Ui_MainWindow(object):
    def __init__(self):
        self.i = 0
        self.enterTask = None
        self.checkBox = None
        self.taskCounter  =None

    # Function to add task in text list and show them in a listView Widget 
    def addTaskCommand(self):
        text = self.enterTask.toPlainText()
        tasks.append(text)
        self.i+=1
        self.taskCounter.setProperty("intValue",self.i)
        self.enterTask.clear()
        self.taskList.addItem(f"{text[0]} -   {text}")

    #Function to save task and print them on a text file called "Tasks.txt"
    def saveTasksCommand(self):
        saveTasks = open("Tasks.txt","w")
        saveTasks.write("----------MY TASKS----------\n\n")
        for i in range(len(tasks)):
            saveTasks.write(tasks[i]+"\n")
        saveTasks.close()
    
    #Function to delete task and also from tasks list (data base)
    def deleteTaskCommand(self):
        selectedTask = self.taskList.currentItem()
        row = self.taskList.row(selectedTask)
        self.taskList.takeItem(row)
        index = int(row)
        tasks.pop(index)
        self.i-=1
        self.taskCounter.setProperty("intValue",self.i)
    # Function to update Tasks list and show updated item on viewList Widget
    def updateTaskCommand(self):
        selectedTask=self.taskList.currentItem()
        text = self.enterTask.toPlainText()
        self.enterTask.clear()
        row = self.taskList.row(selectedTask)
        index = int(row)
        tasks.pop(index)
        tasks.append(text)
        self.taskList.takeItem(row)
        self.taskList.addItem(f"{text[0]} -   {text}")    
    # Main function which creates the whole Main Window using pyqt5
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 704)
        MainWindow.setStyleSheet("background-color: #383737;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.taskList = QtWidgets.QListWidget(self.centralwidget)
        self.taskList.setGeometry(QtCore.QRect(0, 120, 401, 531))
        self.taskList.setObjectName("taskList")
        self.taskList.setStyleSheet("font-size: 25pt;background-color:#302d2d;border:2px solid black;")
        self.enterTask = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enterTask.setGeometry(QtCore.QRect(460, 410, 361, 41))
        self.enterTask.setObjectName("enterTask")
        self.enterTask.setStyleSheet("font-size: 16pt;background-color:#302d2d;")
        self.addTask = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.addTask.setGeometry(QtCore.QRect(460, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        self.addTask.setFont(font)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.addTask.setIcon(icon)
        self.addTask.setObjectName("addTask")
        self.addTask.clicked.connect(self.addTaskCommand)
        self.updateTask = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.updateTask.setGeometry(QtCore.QRect(700, 480, 111, 31))
        self.updateTask.clicked.connect(self.updateTaskCommand)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        self.updateTask.setFont(font)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.updateTask.setIcon(icon)
        self.updateTask.setObjectName("updateTask")
        self.deleteTask = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.deleteTask.setGeometry(QtCore.QRect(580, 520, 121, 31))
        self.deleteTask.clicked.connect(self.deleteTaskCommand)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        self.deleteTask.setFont(font)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.deleteTask.setIcon(icon)
        self.deleteTask.setObjectName("deleteTask")
        self.header2 = QtWidgets.QLabel(self.centralwidget)
        self.header2.setGeometry(QtCore.QRect(550, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(20)
        self.header2.setFont(font)
        self.header2.setObjectName("header2")
        
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(420, 140, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(55)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.taskCounter = QtWidgets.QLCDNumber(self.centralwidget)
        self.taskCounter.setGeometry(QtCore.QRect(110, 60, 141, 51))
        self.taskCounter.setObjectName("taskCounter")
        self.taskCounter.setStyleSheet("color: red;background-color:#383737;border:none;")
        self.saveTasks = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.saveTasks.setGeometry(QtCore.QRect(330, 80, 71, 41))
        self.saveTasks.clicked.connect(self.saveTasksCommand)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        self.saveTasks.setFont(font)
        icon = QtGui.QIcon.fromTheme("font-x-generic")
        self.saveTasks.setIcon(icon)
        self.saveTasks.setObjectName("saveTasks")
        self.taskList.raise_()
        self.enterTask.raise_()
        self.addTask.raise_()
        self.updateTask.raise_()
        self.deleteTask.raise_()
        self.header2.raise_()
        self.MainLabel.raise_()
        self.saveTasks.raise_()
       
        self.taskCounter.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTask.setText(_translate("MainWindow", "ADD TASK"))
        self.updateTask.setText(_translate("MainWindow", "Update Task"))
        self.deleteTask.setText(_translate("MainWindow", "DELETE TASK"))
        self.header2.setText(_translate("MainWindow", "ENTER TASK"))
        self.MainLabel.setText(_translate("MainWindow", "TO DO LIST"))
        self.saveTasks.setText(_translate("MainWindow", "SAVE"))

# Its time to execute our created functions !
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# The End
