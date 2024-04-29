from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

#Funcions
class Pitanje():
    def __init__(self, pitanje, CorrAnsw, W1, W2, W3):
        self.pitanje = pitanje
        self.CorrAnsw = CorrAnsw
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3

def show_q():
    AnswerBox.hide()
    RadioGroupBox.show()
    btn.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_ans():
    AnswerBox.show()
    RadioGroupBox.hide()
    btn.setText("Next question")

def show_hide():
    if btn.text() == "Answer":
        check_ans()
    else:
        next_q()

def ask(q):
    question.setText(q.pitanje)
    shuffle(answers)
    answers[0].setText(q.CorrAnsw)
    answers[1].setText(q.W1)
    answers[2].setText(q.W2)
    answers[3].setText(q.W3)
    yesno.setText(q.CorrAnsw)
    show_q()

def next_q():
    main_win.ukupno += 1
    trenutno_pitanje = randint(0, len(questions)-1)
    ask(questions[trenutno_pitanje])


def check_ans():
    if answers[0].isChecked():
        show_corr("Correct!")
        main_win.correct += 1
        print("You answered", main_win.ukupno, "questions \nYou answered right", main_win.correct, "questions")
        print("Rating:", (main_win.correct/main_win.ukupno)*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corr('Incorrect')
            print("You answered", main_win.ukupno, "questions \nYou answered right", main_win.correct, "questions")

def show_corr(res):
    answer.setText(res)
    show_ans()
#Main window
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 550)

#Labels
question = QLabel("Which nationality does not exist?")
answer = QLabel("Your answer is:")
yesno = QLabel("Correct/Incorrect")


#QGroupBox create
AnswerBox = QGroupBox("Answer Results")
RadioGroupBox = QGroupBox("Answer options")

#Push&Radio Button
btn = QPushButton("Answer")
rbtn_1 = QRadioButton("Enets")
rbtn_2 = QRadioButton("Smurfs")
rbtn_3 = QRadioButton("Chulyms")
rbtn_4 = QRadioButton("Aleuts")
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#RadioButton Group
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#question box layout
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_main = QVBoxLayout()

#radiobutton layout
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

#RadioFroupBox Layout
RadioGroupBox.setLayout(layout_ans1)

#Andswer box layout
hl = QHBoxLayout()
h2 = QHBoxLayout()
vl = QVBoxLayout()

hl.addWidget(answer)
h2.addWidget(yesno)
vl.addLayout(hl)
vl.addLayout(h2)

AnswerBox.setLayout(vl)

#line1
line1 = QHBoxLayout()
line1.addStretch(1)
line1.addWidget(question, stretch = 20, alignment = Qt.AlignCenter)
layout_main.addLayout(line1)
#line2
line2 = QHBoxLayout()
line2.setStretch(1, 10)
line2.addWidget(RadioGroupBox, stretch = 4,alignment = Qt.AlignCenter)
line2.addWidget(AnswerBox, stretch = 4,alignment = Qt.AlignCenter)
layout_main.addLayout(line2)
#line3
line3 = QHBoxLayout()
line3.setStretch(5, 16)
line3.addWidget(btn, stretch = 8, alignment = Qt.AlignCenter) 
layout_main.addLayout(line3)
#show/hide
RadioGroupBox.show()
AnswerBox.hide()
#statistika
main_win.ukupno = 0
main_win.correct = 0
#ask
questions = list()
questions.append(Pitanje("In what time does kurs begin","13h", "11h", "12h", "14h" ))
questions.append(Pitanje("How many colors are there in rainbow","7", "6", "5", "8" ))
questions.append(Pitanje("Whats the fastest land animal", "gepard", "lion", "zebra", "ronaldo" ))
questions.append(Pitanje("The national language of Brazil", "Portuguese", "Spanish", "Italian", "Brazilian"))

next_q()

#click
btn.clicked.connect(show_hide)
#main win
main_win.setLayout(layout_main)
main_win.show()
app.exec_()
