# Дан список чисел, необходимо развернуть без использования метода reverse и функции reversed,
# а также дополнительного списка и среза

def revers(new_list):
    s = len(new_list)-1
    while s != -1:
        new_list.append(new_list[s])
        del new_list[s]
        s -= 1
    print(new_list)

revers([1, 2, 3, 4, 5, 6])