#  программу добавлен дополнительный функционал:
#  проверка на наличие недопустимых символов

print ( 'Введите строку из цифр.n\Можно использовать один из 3-х разделителей: запятую, точку с запятой, слэш ')
correct = 0
while correct==0:
    input_string = input('>>')
    splitter_mask = int(',' in input_string) + (int(';' in input_string) << 1) + (int('/' in input_string) << 2)
    splitter_sign = ''
    if splitter_mask == 0:
        if len(input_string) == 0:
            print('Некорректный ввод! Введена пустая строка.')
        else:
            print('Некорректный ввод! Разделители не найдены.')
    elif splitter_mask == 1:
        splitter_sign = ','
    elif splitter_mask == 2:
        splitter_sign = ';'
    elif splitter_mask == 4:
        splitter_sign = '/'
    else:
        print('Некорректный ввод! Использовано несколько разделителей.')
    if splitter_sign != '':
        list_of_digits = input_string.split(splitter_sign)
        correct = 1
        for elem in list_of_digits:
            if not elem.isdigit():
                correct = 0
    if correct == 0:
        print('Некорректный ввод! В строке найдены недопустимые символы.')
list_unique = []
for elem in list_of_digits:
    if list_of_digits.count(elem) == 1:
        list_unique.append(elem)
if len(list_unique) > 0:
    list_unique.sort()
else:
    print ('Во введенной подстроке нет уникальных символовю.')

