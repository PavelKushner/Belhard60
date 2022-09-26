# Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число,
# пример: [1,2,3,4,5,6,7] N = 3 ответ [5,6,7,1,2,3,4]

def func(N):
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    n = 0
    for i in range(len(new_list)):
        while n != N:
            new_list.append(new_list[i])
            del new_list[i]
            n += 1
    print(new_list)


func(int(input()))
