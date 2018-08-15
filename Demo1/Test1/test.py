
# list = [3,1,2,4,6,5,4,9,4,1,3,2]
# list = [1,2,4,3,6,5]
# print(list)
# for i in range(len(list) - 1):
#     for j in range(len(list)- 1):
#         if list[j+1] < list[j]:
#             list[j+1], list[j] = list[j], list[j+1]
# print(list)
# def func(list):#冒泡排序
#     for i in range(len(list)-1):
#         for j in range(len(list) - i - 1):
#             if list[j] < list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     return list
# list = func(list)
# print(list)
# def func1(list):#选择排序
#     for i in range(len(list) -1 ):
#         for j in range(i+1,len(list)):
#             if list[i] < list[j]:
#                 list[i], list[j] =  list[j], list[i]
#     return list
# func1(list)
# print(list)

# import random
# list = []
# for i in range(10):
#     list.append(random.randint(0, 100))
# ## 快速排序
# def func2(list):#递增
#     if len(list) <= 1:
#         return list
#     i = 0
#     j = len(list)
#     while True:
#         for i in range(i, len(list)):#从左向右
#             if list[i] > list[0]:
#                 break
#         for j in range(0, j)[::-1]:#从右向左
#             if list[j] < list[0]:
#                 break
#         if i >= j:
#             break
#         list[i], list[j] = list[j], list[i]
#     list[j], list[0] = list[0], list[j]
#     list[0:j] = func2(list[0:j])
#     list[j + 1:len(list)] = func2(list[j + 1:len(list)])
#     return list
# print(list)
# print(func2(list))



# with open('a.txt', 'a', encoding='utf-8')as f:
#     for i in range(10):
#         f.write(str(list)+'\n')


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import codecs
import time
import datetime
import os
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 181, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 331, 301))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 10, 341, 301))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 330, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 330, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(self.codeCouner)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.openfile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "代码统计器"))
        self.pushButton.setText(_translate("MainWindow", "添加文件夹"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭软件"))
        self.pushButton_3.setText(_translate("MainWindow", "统计代码"))

    def openfile(self):
        directory1=QFileDialog.getExistingDirectory(self,"请选择Python源文件夹","/")
        setText1(directory1)
        for i in listq:

           self.textEdit.append(str(i))

    def codeCouner(self):
        timeCount()
        codeCount()
        listSplitTime()
        for (key,value) in dict_time_code.items():
            str1=key+':写了'+str(value)+"行代码！"
            self.textEdit_2.append(str1)
listq=[]
dict_time={}
dict_time_code={}
dict_code={}
dict_sortcode={}
timeset={}
def setText1(Dir):
    global listq
    for dirpath, dirnames, filenames in os.walk(Dir):
        for filepath in filenames:
            if str(filepath).endswith(".py"):
               os.path.join(dirpath, filepath)
               str1=str(os.path.join(dirpath, filepath))
               listq.append(str1)

def timeCount():
    global dict_time
    for i in listq:
        dict_time[i]=TimeStampToTime(os.path.getctime(i))
        print(dict_time[i])

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d ',timeStruct)

def codeCount():
    global dict_code
    for i in listq:
        dict_code[i]=len(codecs.open(i, 'rU', 'utf-8').readlines())

def listSplitTime():
        timeset=set(dict_time.values())
        for i in iter(timeset):
            dict_time_code[i]=0
        for i in iter(timeset):
            for j in listq:
                if dict_time[j]==i:
                    dict_time_code[i]+=dict_code[j]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
