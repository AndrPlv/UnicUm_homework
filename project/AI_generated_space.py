import tkinter as tk
import os



root = tk.Tk()
root.geometry('350x450')
root.resizable(False, False)
root.title('main')

spaceF = [0,160,8239,8203,8195,8194,8199,8200,8201,12288,8232,8233,133]

def keys():
    name_file = entry1.get()
    all_file = os.listdir(os.getcwd())
    if name_file in all_file and name_file[name_file.index("."):] == '.txt':
        return 1
    else:
        text3 = tk.Label(text='Допущена ошибка в имени файла')
        text3.place(x=50,y=350)
        root.after(1000, lambda: text3.destroy())
        return 0

def open1():
    key = keys()
    if key:
        with open(entry1.get(), 'r', encoding='utf-8') as file:
            info = file.read()
            for j in info:
                if ord(j) in spaceF:
                    info = info.replace(j, ' ')
        with open(entry1.get(), 'w', encoding='utf-8') as file:
            file.write(info)
            text3 = tk.Label(text=f'Содержимое переписанно.')
            text3.place(x=50, y=350)
            root.after(1000, lambda: text3.destroy())
def open2():
    key = keys()
    space = 0
    if key:
        with open(entry1.get(), 'r', encoding='utf-8') as file:
            text = file.read()
            for j in text:
                if ord(j) in spaceF:
                    space += 1
            if space:
                text3 = tk.Label(text=f"Обнаружено {space} 'AI generated space'.")
                text3.place(x=50, y=350)
                root.after(1000, lambda: text3.destroy())
            else:
                text3 = tk.Label(text="'AI generated space' не обнаружено.")
                text3.place(x=50, y=350)
                root.after(1000, lambda: text3.destroy())

def open3():
    key = keys()
    space = 0
    if key:
        with open(entry1.get(), 'r', encoding='utf-8') as file:
            text = file.read()
            for j in text:
                if ord(j) in spaceF:
                    space += 1
        if space > 0:
            with open(entry1.get(), 'r', encoding='utf-8') as file:
                info = file.read()
                for obj in info:
                        if ord(obj) in spaceF:
                            info = info.replace(obj, ' ')
            with open(f'new_{entry1.get()}', 'w', encoding='utf-8') as file:
                    file.write(info)
            text3 = tk.Label(text=f'Содержимое переписанно и хранится\n в файле new_{entry1.get()}.')
            text3.place(x=50, y=350)
            root.after(1000, lambda: text3.destroy())
        else:
            text3 = tk.Label(text=f"Файл итак не содержит 'AI generated space'.")
            text3.place(x=50, y=350)
            root.after(1000, lambda: text3.destroy())
text1 = tk.Label(text='Здравствуйте! \nЭто программа для удаления коротких пробелов.')
text1.place(x=20,y=30)


text2 = tk.Label(text='Введите путь к файлу:')
text2.place(x=40,y=100)

entry1 = tk.Entry(root, width=40)
entry1.place(x=40,y=130)

button1 = tk.Button(text='Открыть и изменить', width=20,height=2, command=open1)
button1.place(x=40,y=180)

button2 = tk.Button(text='Проверить',width=10,height=2, command=open2)
button2.place(x=230,y=180)

button3 = tk.Button(text='Записать в новый файл', width=20,height=2, command=open3)
button3.place(x=100,y=260)

root.mainloop()
