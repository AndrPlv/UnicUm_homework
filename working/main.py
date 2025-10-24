print('Введите размер поля (формат X:Y): ')
size_pole = input(">>> ").split(":")
matrix = [['0' for _ in range(int(size_pole[0]))] for _ in range(int(size_pole[1]))]
print('Текущее местоположение робота (формат X:Y)')
cord_robot = input(">>> ").split(":")
matrix[cord_robot[0]][cord_robot[1]] = 'R'
S = [[cord_robot[0],cord_robot[1]]]
print('Укажите директорию имя или путь относительно этого файла (Например: alg.txt, /algs/alg.txt)')
name_file = input(">>> ")

command = []

with open(f'UnikUm/{name_file}', 'r', encoding='UTF-8') as file:
    plan = file.read().split('\n')
for command in plan:
    pass
