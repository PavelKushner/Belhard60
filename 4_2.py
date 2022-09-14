# Без использования collection, написать программу, которая будет создавать словарь для подсчитывания количества вхождений
# каждой буквы в текст введенный с клавиатуры.
text = input()
new_text = {text[i]: text.count(text[i]) for i in range(len(text))}
print(new_text)
