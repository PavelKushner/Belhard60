# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных.
number_1, number_2, number_3 = float(input()), float(input()), float(input())
below_0 = str(number_1).startswith('-') + str(number_2).startswith('-') + str(number_3).startswith('-')
above_0 = bool(number_1) + bool(number_2) + bool(number_3) - below_0
print('положительных чисел =', above_0)
print('отрицательных чисел =', below_0)
