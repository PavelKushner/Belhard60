# Пользователь вводит предложение, заменить все пробелы на '-' 2-мя способами.
text = input()
text_new = text.split()
text = '-'.join(text_new)
print(text)

text = input()
print(text.replace(' ', '-'))