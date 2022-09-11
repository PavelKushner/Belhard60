number_degree = int(input())
new_list = []
for i in range(number_degree+1):
    number = 2**i
    new_list.append(number)
print(new_list)
