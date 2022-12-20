#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'В этом тексте нужно удалить абв. Может и "абв"'


def del_text(text: object) -> object:
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text_new = del_text(text)
print(text_new)