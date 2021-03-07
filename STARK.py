from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import wikipedia
import wolframalpha
import speech_recognition as sr
import pyttsx3
import sys
import socket
hostname = socket.gethostname()

app= QApplication(sys.argv)
win=QMainWindow()
win.setStyleSheet('background-color:#000000;')
win.setFixedSize(710,410)
win.setWindowTitle("Stark")

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

myline=QtWidgets.QLineEdit(win)
myline.setPlaceholderText('Ask Me Anything...')
myline.returnPressed.connect(myacction)
myline.resize(600,35)
myline.move(30,20)
myline.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0066b7')
myline.setFont(QFont('LEMON MILK', 12))

b1=QtWidgets.QPushButton(win)
b1.setText("Speak")
b1.clicked.connect(saysomething)
b1.setFixedSize(60,35)
b1.move(640,20)
b1.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0079d8')
b1.setFont(QFont('LEMON MILK', 10))

l1=QtWidgets.QTextEdit(win)
l1.move(30,60)
l1.setFixedSize(600,310)
l1.setStyleSheet('border:5px solid #003661; background-color:#000000; color:#0066b7')
l1.setFont(QFont('LEMON MILK', 12))

speakText("Welcome "+hostname)
win.show()
sys.exit(app.exec_())