# Пользователь вводит предложение, заменить все пробелы на '-' 2-мя способами.
text = input()
text_new = []
for i in range(len(text)):
    if text[i] == ' ':
        text_new.append('-')
    else:
        text_new.append(text[i])
print(*text_new, sep='')
