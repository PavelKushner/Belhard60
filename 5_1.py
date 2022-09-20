# Ввести первые N чисел кратные M и больше К
N = int(input('Введи колличество выводимых чисел:'))
M = int(input('Введи число для проверки на кратность: '))
K = int(input('Число, которое не должно превышать выводимое число:'))
num = 0
numbers = []
counter = K
while num != N:
    counter += 1
    if counter % M == 0:
        numbers.append(counter)
        num += 1
print(numbers)
