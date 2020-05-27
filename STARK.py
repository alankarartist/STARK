from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import wikipedia
import wolframalpha
import speech_recognition as sr
import pyttsx3
import sys
import socket
hostname = socket.gethostname()

app= QApplication(sys.argv)
win=QMainWindow()
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
        print("Google Speech Recognition Could not understand auido")

def myacction():
    input = myline.text()
    if len(input) >= 1:
        try:
            myappid= wolframalpha.Client('QHR7WJ-52AL3EQWU4')
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
myline.resize(600,25)
myline.move(30,20)

b1=QtWidgets.QPushButton(win)
b1.setText("Speak")
b1.clicked.connect(saysomething)
b1.setFixedSize(60,25)
b1.move(640,20)

l1=QtWidgets.QTextEdit(win)
l1.move(30,50)
l1.setFixedSize(600,300)

speakText("Welcome "+hostname)
win.show()
sys.exit(app.exec_())