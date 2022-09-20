# Ввести первые N чисел кратные M и больше К
N = int(input('Введи колличество выводимых чисел:'))
M = int(input('Введи число для проверки на кратность: '))
K = int(input('Число, которое не должно превышать выводимое число:'))
num = 0
numbers = []
while num != N:
    number = int(input('Введи число:'))
    if number % M == 0 and number > K:
        numbers.append(number)
        num += 1
print(numbers)
