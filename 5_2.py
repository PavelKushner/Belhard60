# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число.
number_1 = int(input('Введи первое число: '))
effect = input('Что нужно сделать?: ')
while effect not in '+-/**':
    print('Такого действия не существует. Повтори операцию!')
    effect = input('Что нужно сделать?: ')
number_2 = int(input('Введи второе число: '))
try:
    if effect == '+':
        print(number_1 + number_2)
    elif effect == '-':
        print(number_1 - number_2)
    elif effect == '*':
        print(number_1 * number_2)
    elif effect == '/':
        print(number_1 / number_2)
    elif effect == '**':
        print(number_1 ** number_2)
except ZeroDivisionError as e:
    print('на ноль делить нельзя!')