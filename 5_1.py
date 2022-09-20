# Ввести первые N чисел кратные M и больше К
N = int(input('Введи колличество выводимых чисел:'))
M = int(input('Введи число для проверки на кратность: '))
K = int(input('Число, которое не должно превышать выводимое число:'))
num = 0
numbers = []
while num != N:
    K += 1
    if K % M == 0:
        numbers.append(K)
        num += 1
print(numbers)
