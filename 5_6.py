# Вводятся две строки, a и b, и возвращать количество раз, когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв
a = input()
b = input()
counter = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and i == j:
            counter += 1
print(counter)