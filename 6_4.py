# Дан список содержащий в себе различные типы данных, отфильтровать таким образом, чтобы остались только строки,
# использование дополнительного списка незаконно.


def func(grand_list):
    s = len(grand_list)
    for i in range(s):
        if type(grand_list[i]) != type(''):
            del grand_list[i]
    #return grand_list
    print(grand_list)

#grand_list = [1, 2, 1, 1, 123]

func([1, 2, 1, 1, 123])