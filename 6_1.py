# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def translate_binary(dec_num):
    new_dijit = []
    while dec_num != 0:
        new_dijit.append(dec_num % 2)
        dec_num = dec_num // 2
    new_dijit = new_dijit[::-1]
    print('Число в двоичной системе:', *new_dijit, sep='')

def translate_dec(binary_num):
    new_dec_num = 0
    c = 1
    s = len(binary_num)
    for i in range(s):
        if binary_num[i] != 0:
            new_dec_num += (2*int(binary_num[i]))**(s-c)
            c += 1
        else:
            c += 1
    print('Число в десятичной системе:', new_dec_num)

print('Введи десятичное число:')
translate_binary(int(input()))
print('Введи двоичное число:')
translate_dec(input())
