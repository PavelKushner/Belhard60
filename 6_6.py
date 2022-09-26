# Дан список рандомных чисел, необходимо отсортировать его ввиде, сначала четные потом нечетные.

def new_sort(new_list):
    new_list2 = sorted(new_list, key=lambda x: (x%2, x))

    print(new_list2)


new_sort([1, 2, 3, 4, 5, 6])