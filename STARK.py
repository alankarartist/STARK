from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import wikipedia
import wolframalpha
import speech_recognition as sr
import pyttsx3
import sys
import socket
import os

hostname = socket.gethostname()
cwd = os.path.dirname(os.path.realpath(__file__))
app= QApplication(sys.argv)
win=QMainWindow()
win.setStyleSheet('background-color:#000000;')
win.setFixedSize(710,440)
win.setWindowTitle("STARK")
win.setWindowIcon(QIcon(os.path.join(cwd+'\\UI\\icons', 'stark.png')))
win.setWindowFlags(QtCore.Qt.FramelessWindowHint)

def speakText(command):
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait()

def saysomething():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("You said: " + r.recognize_google(audio))
        myline.setText(r.recognize_google(audio))
        myacction()
    except:
        print("Google Speech Recognition Could not understand audio")

def myacction():
    input = myline.text()
    if len(input) >= 1:
        try:
            myappid= wolframalpha.Client('XXXXXXXXXXXXXXXXXX')
            res = myappid.query(input)
            ans = next(res.results).text
            l1.setText(ans)
            speakText(ans)
        except:
            l1.setText(wikipedia.summary(input))
            speakText(wikipedia.summary(input, sentences = 2))
    else:
        speakText("Didn't get that")

widget = QWidget(win)
widget.resize(710,30)
widget.setStyleSheet("QWidget{\n"
"    background-color:rgb(20,20,20);\n"
"}\n"
"QLabel{\n"
"    background-color:rgb(20,20,20);\n"
"}\n"
"QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgb(144,144,144);\n"
"    font:bold;\n"
"    font-size:15px;\n"
"    font-family:OnePlus Sans Display;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
label = QLabel(widget)
label.resize(30,30)
label.move(10,0)
label.setStyleSheet('background-color:rgb(20,20,20); color:rgb(144,144,144);')
label.setFont(QFont('OnePlus Sans Display', 10))
label.setMinimumSize(QtCore.QSize(30, 30))
label.setMaximumSize(QtCore.QSize(30, 30))
label.setAutoFillBackground(False)
label.setStyleSheet(" background-color:rgb(20,20,20);")
label.setText("")
label.setPixmap(QtGui.QPixmap(os.path.join(cwd+'\\UI\\icons', 'stark.png')))
label.setScaledContents(True)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setWordWrap(False)
label_2 = QLabel(widget)
label_2.move(40,0)
label_2.resize(630,30)
font = QtGui.QFont()
font.setFamily("OnePlus Sans Display Medium")
font.setPointSize(12)
font.setBold(False)
font.setWeight(50)
label_2.setFont(font)
label_2.setStyleSheet("color:rgb(144,144,144);")
label_2.setAlignment(QtCore.Qt.AlignCenter)
label_2.setText("STARK")
pushButton = QPushButton(widget)
pushButton.setMinimumSize(QtCore.QSize(30, 28))
pushButton.setMaximumSize(QtCore.QSize(30, 28))
font = QtGui.QFont()
font.setFamily("OnePlus Sans Display")
font.setPointSize(8)
font.setBold(True)
font.setItalic(False)
font.setWeight(75)
pushButton.setFont(font)
pushButton.setFlat(True)
pushButton.move(670,0)
pushButton.resize(30,30)
pushButton.setStyleSheet("color:rgb(144,144,144);")
pushButton.setText('x')
pushButton.clicked.connect(win.close)

myline=QtWidgets.QLineEdit(win)
myline.setPlaceholderText('Ask Me Anything...')
myline.returnPressed.connect(myacction)
myline.resize(600,35)
myline.move(30,50)
myline.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0066b7')
myline.setFont(QFont('OnePlus Sans Display', 12))

b1=QtWidgets.QPushButton(win)
b1.setText("SPEAK")
b1.clicked.connect(saysomething)
b1.setFixedSize(60,35)
b1.move(640,50)
b1.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0079d8')
b1.setFont(QFont('OnePlus Sans Display', 10))

l1=QtWidgets.QTextEdit(win)
l1.move(30,90)
l1.setFixedSize(600,310)
l1.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0066b7')
l1.setFont(QFont('OnePlus Sans Display', 12))

speakText("Welcome "+hostname)
win.show()
sys.exit(app.exec_())