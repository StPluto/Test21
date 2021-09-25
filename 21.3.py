#!/usr/bin/env python3
# -*- config: utf-8 -*-

from pydoc import text
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


# измените программу из п. 9 так, чтобы открытие и сохранение файлов
# выполнялось не через экземпляры Button , а через Menu . Команду очистки текстового поля
# поместите в контекстное меню.

def del_text():
    answer = mb.askokcancel('Удаление текста', 'Реально удалить?')
    if answer:
        text.delete(1.0, END)


def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
    except (FileNotFoundError, TypeError):
        mb.showinfo("Файл не выбран!,Преобразовать")
    else:
        s = f.read()
        text.insert(1.0, s)
        f.close()


def extract_text():
    file_name = fd.asksaveasfilename()
    try:
        f = open(file_name, 'w')
    except (FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла,Файл не сохранен!")
    else:
        s = text.get(1.0, END)
        f.write(s)
        f.close()


root = Tk()

mainmenu = Menu()
root['menu'] = mainmenu
mainmenu.add_command(label="Открыть", command=insert_text)
mainmenu.add_command(label="Сохранить", command=extract_text)

text = Text(width=50, height=25)
text.pack()

popupmenu = Menu(text, tearoff=0)
popupmenu.add_command(label="Очистить", command=del_text)

text.bind('<Button-3>',
          lambda event: popupmenu.post(event.x_root, event.y_root))

root.mainloop()
