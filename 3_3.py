# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем формотирования 3-мя способами.
name, age, town = input(), input(), input()
print('Добрый день. Меня зовут {name}. Мне {age} лет. Я из города {town}.'.format(name=name, age=age, town=town))

name, age, town = input(), input(), input()
print(f'Добрый день. Меня зовут {name}. Мне {age} лет. Я из города {town}.')

name, age, town = input(), int(input()), input()
print('Добрый день. Меня зовут %s. Мне %d лет. Я из города %s.' %(name, age, town))
