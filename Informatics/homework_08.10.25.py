print("Программа для работы со словарями")
print('''Функионал программи:
      1. Вывести весь словарь.
      2. Добавить элемент.
      3. Удалить элемент.
      4. Очистить весь словарь.
      5. Вывести пару по ключу.
      6. Вывести все ключи.
      7. Выход.
      ''')
print()
print("Создание словоря")
dicts = {}
print("Введите длину словоря:")
for _ in range(int(input(">>> "))):
    print("Введите пару форма: 'ключ: значение'")
    data_for_dicts = input(">>> ").split(': ')
    dicts[data_for_dicts[0]] = data_for_dicts[1]
print('Словарь создан')
print("Вместо команды используйте её номер в графе 'Функционал'")
while (True):
    number_command = input(">>> ")
    if number_command == "1":
        for j in dicts:
            print(f'{j}: {dicts[j]}')
    elif number_command == '2':
        print("Введите пару форма: 'ключ: значение'")
        data_for_dicts = input(">>> ").split(': ')   
        dicts[data_for_dicts[0]] = data_for_dicts[1]
    elif number_command == '3':
        print('Ввкдите ключ:')
        del_el = input(">>> ")
        del dicts[del_el]
    elif number_command == '4':
        dicts.clear()
    elif number_command == '5':
        print("Введите ключ:")
        keys = input(">>> ")
        if keys in dicts.keys():
            print(f'{keys}: {dicts[keys]}')
        else:
            print('Ошибка: такого ключа нет в словаре')
    elif number_command == '6':
        print(*dicts.keys())
    elif number_command == '7':
        break
    else:
        print("Мы ёще не добавили такой коианды")
    print()
