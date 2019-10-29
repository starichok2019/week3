# Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран

count = int(input('Введите количество элементов'))
result = []
for i in range(count):
    number = int(input('Введите число'))
    result.append(number)
result.sort()
print(result)

# В программу добавлен функционал:
# контроль ввода только одной цифры, а не числа
list_length = int(input('Введите количество элементов: '))
list_of_digits = []
for i in range(list_length):
    elem = input(f'Введите {i + 1}-й элемент: ')
    while not (elem.isdigit() and len(elem) == 1):
        elem = input('Элементом может быть только одна цифра! Попробуйте ещё раз:')
    list_of_digits.append(elem)
    elem = ''
list_of_digits.sort()
print (list_of_digits)




