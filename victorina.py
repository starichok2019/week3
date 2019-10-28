# В программу добавлен функционал повторного запроса информации, если пользователь ввёлне число.

import random

QUESTIONNAIRE = [
    {'name': 'Ленин Владимир Ильич',          'dob_d': '22.04.1870', 'dob_a': 'двадцать второе апреля 1870 года'},
    {'name': 'Шукшин Василий Макарович',      'dob_d': '25.07.1929', 'dob_a': 'двадцать пятое июля 1929 года'},
    {'name': 'Высоцкий Владимир Семенович',   'dob_d': '25.01.1938', 'dob_a': 'двадцать пятое января 1938 года'},
    {'name': 'Куприн Александр Иванович',     'dob_d': '26.08.1870', 'dob_a': 'двадцать шестое августа 1870 года'},
    {'name': 'Петр 1 Алексеевич (Великий)',   'dob_d': '09.06.1672', 'dob_a': 'девятое июня 1672 года'},
    {'name': 'Чехов  Антон Павлович ',        'dob_d': '29.01.1860', 'dob_a': 'двадцать девятое января 1860 года'},
    {'name': 'Толстой Лев Николаевич',         'dob_d': '09.09.1828', 'dob_a': 'девятое  сентября 1828 года'},
    {'name': 'Есенин  Сергей Александрович',   'dob_d': '03.10.1895', 'dob_a': 'третье октября 1895 года'},
    {'name': 'Пушкин  Александр Сергеевич',    'dob_d': '06.06.1799', 'dob_a': 'шестое  июня 1799 года'},
    {'name': 'Гоголь Николай Васильевич',      'dob_d': '01.04.1809', 'dob_a': 'первое  апреля 1809 года'},
]
ASK = 'Напишите дату рождения данного известного человека в формате "дд.мм.гггг":\n'
i = 0
correct =0
incorrect = 0
selection = random.sample(range(10), 5)

print('Викторина: "Известные люди России"\n')

while True:
    if i == len(selection):
        print(f'Правильных ответов: {correct}.\n'
              f'Неправильных ответов: {incorrect}.\n'
              f'Процент правильных ответов: {correct * 100/i}%.\n'
              f'Процент неправильных ответов: {incorrect * 100/i}%.\n\n')
        ans = input('Желаете пройти тест ещё раз? ( Да / Нет)')
        if ans.lower() == 'да':
            i = 0
            correct = 0
            incorrect = 0
        else:
            break
    print(f"{i+1}. {ASK}{QUESTIONNAIRE[selection[i]]['name']}.")
    ans = input('>>>')
    if ans[:2].isdigit() and [2] == '.' and ans[3:5].isdigit() and ans[5] == '.' and ans[6:].isdigit():
        if ans == QUESTIONNAIRE[selection[i]]['dob_d']:

            correct +=1
        else:
            incorrect +=1
            print(f"Неверно. Правильный ответ: {QUESTIONNAIRE[selection[i]]['dob_a']}")
        i +=1
    else:
        print('некорректный формат ввода данных. Поробуйте ещё раз.')