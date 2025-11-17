from random import randint
import string
import os
import json
need_info = ['Полное ФИО','Пол','Телефон']
def write(dic: dict, file='info.json'):
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/{file}', 'a', encoding='utf-8') as file:
        json.dump(dic, file, ensure_ascii=False)
def read(name='info.json'):
    path = f'{os.path.dirname(os.path.abspath(__file__))}/{name}'
    if os.path.getsize(path):
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    return {}
def clear(name="info.json"):
    path = f'{os.path.dirname(os.path.abspath(__file__))}/{name}'
    open(f'{os.path.dirname(os.path.abspath(__file__))}/{name}', 'w').close()
def rash(text: str):
    text_out = ''
    sdv = randint(10,100)
    for j in text:
        text_out += f'{ord(j) + sdv}&'
    text_out += f'{sdv}&'
    return text_out
def derash(text: str):
    text_out = ''
    r = text[-1]
    text = text.split(r)
    sdv = text[-2]
    for j in text[:-2]:
        text_out += f'{chr(int(j) - int(sdv))}'
    
    return text_out
def password():
    while(True):
        print('Введите пороль:')
        password = input(">>> ")
        a=b=c=0
        for j in password:
            if j in string.punctuation:
                a=True
            elif j in string.ascii_uppercase or j in [chr(j) for j in range(ord("А"),ord("Я"))]:
                b=True
            elif j in string.ascii_lowercase or j in [chr(j) for j in range(ord("а"),ord("я"))]:
                c=True
        if a==1 and b==1 and c==1:
            print("Пороль надёжен")
            return password
        print("Пороль не надёжен")   
def update(new_data: dict, file='info.json'):
    data = read()
    clear()
    write({**data, **new_data})   
def input_info(file='info.json', check_list=need_info):  
    print("Введите основную информацию:")
    print('\nКак Вас называть?')
    name = input(">>> ")
    data = read()
    for user in data:
            if name == user:
                print("Пользователь с таким именем уже зарегестрирован.")
                os._exit(0)
            else:
                pass
    passw = password()
    user_info = []

    for j in check_list:
        print(f'{j}:')
        if j == 'Телефон':          
            tele_number = input(">>> ")
            tele_number = tele_number.replace(' ', '', tele_number.count(''))
            data = read()
            if data != {}:
                for user in data:
                    obj = data[user]
                    if obj == tele_number:
                        print("Пользователь с таким номером телефона уже зарегестрирован.")
                        os._exit(0)
                user_info.append(rash(tele_number))
            else:
                user_info.append(rash(tele_number))                   
        else:
            user_info.append(rash(input(">>> ")))            

    print("Введите свою дату рождения:")
    years_info = ['День', 'Месяц', 'Год'] 
    years =[rash(j) for j in input(">>> ").split('.')]
    data = {name: {**dict(zip(['Пороль'],[rash(passw)])),**dict(zip(years_info,years)),**dict(zip(need_info,user_info)), **dict(zip(["Баланс"], [rash('0')]))}}
    update(data)
def update_user(user: str,datas: dict):
    data = read()
    data[user] = datas
    clear()
    write(data)
def edit_info(user: str,check_list=need_info):
    print("Что вы хотите редактировать(выбрать из списка)")
    print(*check_list)
    p = input('>>> ')
    print("Новая информация:")
    new_data = input(">>> ")
    data = (read())[user]
    data[p] = rash(new_data)
    update_user(user,data)
def openAcc(file='info.json',rash=True):
    data = read(file)
    print("Ввеите имя пользователя")
    user_in = input(">>> ")
    if user_in in list(data.keys()):
        print("Пользователь найден")
        passw_t = derash(data[user_in]['Пороль'])
        print("Пороль:")
        passwords = input(">>> ")
        if passwords == passw_t:
            print("Вы вошли")
            return user_in
        else:
            while not(passw_t == passwords):
                print("Пороль не верный, введите повторно:")
                passw = input(">>> ")
                if passw == passw_t:
                    print("Вы вошли")
                    return user_in    
    else: 
        print("Пользователь не найден")
        return -1
def edit(user: str,info: dict):
    data = read()
    user = data[user]
    print(user)    
def input_many(user):
    print("Сколько денег ввести(в рублях):")
    many = int(input(">>> "))
    while(many<0):
        print("Вы не можете ввести отрицательную сумму")
        print("Сколько денег ввести(в рублях):")
        many = int(input(">>> ")) 
    many = str(many)      
    dat = read()
    if 'Баланс' in dat[user].keys():
        bal = int(derash(dat[user]['Баланс']))
        bal += int(many)
        dat[user]['Баланс'] = rash(str(bal))
    else:
        dat[user]['Баланс'] = rash(many)    
    update_user(user,dat[user])
def look_balans(user):
    data = (read())[user]
    print(derash(data['Баланс']))
def look_info(user: str):
    print(f"Имя пользователя: {user}")
    data = (read())[user]
    for obj in data:
        print(f"{obj}: {derash(data[obj])}")
edit_info("Andreys")
input_many("Andreys")
look_info("Andreys")