print('Программа для работы со списком книг.')
print('''Функции:
        1. Вывод всего списка.
        2. Поиск по индексу.
        3. Добаление элемента.
        4. Удаление элемента по индексу.
        5. Полная очистка списка.''')
print()
print('Введите все элементы списка через пробел:')
books = input(">>> ").split()
print('Список создан.')
print()
print('Для вызова функции используете её номер.')

while(True):
    print('Комманда:')
    command = input(">>> ")

    if command == "1":
        print(f'-> {books}')
    elif command == "2":
        print("Введите индекс:")
        index = int(input(">>> "))
        if -len(books) <= index < len(books):
            print(f'-> {books[index]}')
        else:
            print("Неверный индекс")
    elif command == "3":
        print("Введите элемент который нужно добавить:")
        books.append(input(">>>"))
    elif command == "4":
        print("Введите индекс элемента который нужно удалить:")
        index = int(input(">>> "))        
        if -len(books) <= index < len(books):
            del books[index]
        else:
            print("Неверный индекс")
    elif command == "5":
            books.clear()

    elif command == 'Стоп':
        break
    else:
        print("Комманда введена не верно")
    print()
