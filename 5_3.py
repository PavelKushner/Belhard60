# Вывесли четные числа от 2 до N по 5 в строку
N = int(input())
b = 0
numbers = []
for i in range(2, N+1):
    if i % 2 == 0:
        numbers.append(i)
        b += 1
        if b % 5 == 0:
            numbers.append(f'\n')
print(*numbers)