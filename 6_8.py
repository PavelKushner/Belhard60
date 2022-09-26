# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой он страны.

new_dict = {'England': 'London', 'France': 'Paris', 'Spain': 'Madrid', 'Italy': 'Rome', 'Germany': 'Berlin'}

def country(capital):
        print(new_dict.get(key[capital]))

country('London')