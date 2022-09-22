# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def translate(dec_num):
    new_dijit = []
    while dec_num != 0:
        new_dijit.append(dec_num % 2)
        dec_num = dec_num // 2
    new_dijit = new_dijit[::-1]
    print('Число в двоичной системе:', *new_dijit, sep='')

    new_dec_num = 0
    c = 1
    s = len(new_dijit)
    for i in range(len(new_dijit)):
        if new_dijit[i] != 0:
            new_dec_num += (2*int(new_dijit[i]))**(s-c)
            c += 1
        else:
            c += 1
    print('Число в десятичной системе:', new_dec_num)

translate(int(input()))
