# Дан список содержащий в себе различные типы данных, отфильтровать таким образом, чтобы остались только строки,
# использование дополнительного списка незаконно.


def func(grand_list):
    s = len(grand_list)
    while s != 0:
        if isinstance(grand_list[s-1], str):
            s -= 1
        else:
            del grand_list[s - 1]
            s -= 1
    print(grand_list)

grand_list = [1, 2, '1', 1, 123, 'dg']
func(grand_list)