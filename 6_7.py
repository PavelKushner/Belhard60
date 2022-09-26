# Дан список чисел, необходимо для каждого элемента посчистать сумму его соседей, для крайних
# чисел одним из соседей является число с противоположной стороны списка

def sum_num(new_list):
    new_list1 = []
    for i in range(len(new_list)):
        if i + 1 != len(new_list):
            new_list1.append(new_list[i - 1] + new_list[i + 1])
        else:
            new_list1.append(new_list[i-1] + new_list[0])

    return new_list1

print(sum_num([1,2,3,4,5]))
