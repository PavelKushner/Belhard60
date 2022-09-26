# Дан список рандомных чисел, необходимо отсортировать его ввиде, сначала четные потом нечетные.

def new_sort(new_list):
    new_list = sorted(new_list, key=lambda x: (x%2, x))

    print(new_list)


new_sort([1, 2, 3, 4, 5, 6])


def new_sort2(new_list2):
    even = list(filter(lambda x: x%2 == 0, new_list2))
    odd = list(filter(lambda x: x%2 != 0, new_list2))

    print(even + odd)

new_sort2([1, 2, 3, 4, 5, 6])