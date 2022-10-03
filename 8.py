text = '''
Мобильный телефон 3000

ru от 1 шт 18000

en от 5 шт 17000

ru от 20 шт 15000

fr от 1 шт 17000
'''
text_1 = list(text.split('\n'))
name = ['Мобильный телефон 3000']
countries = ['ru', 'en', 'fr']
count = ['от 1', 'от 5', 'от 20']
price = ['17000', '18000', '15000']
data_5 = {}
data_4 = {}
for k in range(len(text_1)):
    for c in range(len(countries)):
        for i in range(len(count)):
            for j in range(len(price)):
                if countries[c] in text_1[k] and count[i] in text_1[k] and price[j] in text_1[k]:
                        data_5.setdefault(countries[c], []).append({count[i]: price[j]})
                for s in range(len(name)):
                    if name[s] in text_1[k]:
                        data_4.setdefault(name[s], data_5)

print(data_4)

