#создай приложение для запоминания информ
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

class Question():
    def __init__(self, question,right_answer,wrong1,wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(
    Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(
    Question('национальная хижина якутов', 'ураса' , 'харча', 'ротберунчик','алгоримтка'))
questions_list.append(
    Question('современые языки програмирования', 'питон' , 'бейсик','паскаль','фортан'))
questions_list.append(
    Question('в каком году образовалось алгоритмика в РБ', '2018' , '2015', '2019','2020'))  
questions_list.append(
    Question('кем является андрей?', 'самым лучшем парнем в мире' , 'скромным парнем', 'глупым парнем','обычным парнем'))  
questions_list.append(
    Question('в каком году я родился', '2010' , '2024', '2000','2011'))
questions_list.append(
    Question('где я родился?', 'новополцк' , 'полоцк', 'витебск','минск'))
questions_list.append(
    Question('Какая планета в нашей Солнечной системе самая большая?', 'Юпитер', 'Земля', 'Сатурн', 'Нептун'))
questions_list.append(
    Question('Кто нарисовал Мону Лизу?', 'Леонардо да Винчи' , 'Пабло Пикассо', 'Винсент Ван Гог','Никита Кологривый'))
questions_list.append(
    Question('Сколько градусов в круге?', '360' , '180', '90','150'))


    
app = QApplication([])
window=QWidget()
window.setWindowTitle('Memo Card')
window.resize(400,200)
window.move(100,100)

lb_Question = QLabel('Какой национальности не существует?')
btn_OK=QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1=QRadioButton('ответ1')
rbtn_2=QRadioButton('ответ2')
rbtn_3=QRadioButton('ответ3')
rbtn_4=QRadioButton('ответ4')

RadioGroup= QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно\Неправильно')
lb_Correct = QLabel('Правильный ответ')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignLeft)
AnsGroupBox.setLayout(layout_res)


layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()


layout_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter|Qt.AlignVCenter ))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()



layout_line3.addStretch(5)
layout_line3.addWidget(btn_OK, stretch =5)
layout_line3.addStretch(5)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

def show_result():
    #показать панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    #показать панель ответов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)    
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

    
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Анализ твоего позора\n-Всего легких вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг крутости:', window.score/window.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно!')


def next_question():


    window.total +=1
    print('Анализ твоего позора\n-Всего легких вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(questions_list) - 1) 
    q = questions_list[cur_question]
    ask(q)







def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.setLayout(layout_card)   

window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()
window.show()
app.exec()