# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных.
above_0 = 0
below_0 = 0
for i in range(3):
    number = float(input())
    if number > 0:
        above_0 += 1
    elif number < 0:
        below_0 += 1
print('положительных чисел =', above_0)
print('отрицательных чисел =', below_0)
