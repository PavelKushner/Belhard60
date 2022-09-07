# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных.
number_1, number_2, number_3 = input(), input(), input()
above_0 = 0
below_0 = 0
above_0 += '-' not in number_1 and int(number_1) != 0
above_0 += '-' not in number_2 and int(number_2) != 0
above_0 += '-' not in number_3 and int(number_3) != 0
below_0 += '-' in number_1
below_0 += '-' in number_2
below_0 += '-' in number_3
print('положительных чисел =', above_0)
print('отрицательных чисел =', below_0)
