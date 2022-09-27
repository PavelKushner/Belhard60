# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой он страны.

new_dict = {'England': 'London', 'France': 'Paris', 'Spain': 'Madrid', 'Italy': 'Rome', 'Germany': 'Berlin'}

def country(capital):
        my_list = list(new_dict.items())
        for i in range(len(my_list)):
                if my_list[i][1] == capital:
                        print(my_list[i][0])
        print(my_list)

country('London')