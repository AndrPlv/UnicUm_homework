r'''
                              &
                            / & \
                          / * @ & \
                        / * $ @ ? & \
                      / % $ # @ & # % \
                    / * % ? * & + # @ % \
                  / @ ? * * ? + $ @ @ & % \
                / & + * * & $ % $ + % % # $ \
              / # # ? & & & ? * * * ? ? @ + ? \
            / * * @ & ? % @ ? % # @ + % ? @ & @ \
          / * & % % @ # $ @ # $ & + & $ # + + ? # \
        / @ # $ % & * * @ * @ % ? @ # % * @ # $ % @ \
      / @ @ # + $ # @ % * @ + * % * * & # & # # + # $ \
                    * * * * * * * * * *
                    * * * * * * * * * *
'''

from random import randint,choice

def tre(y: int, sim_1="*",sim_0=" "):
    matrix = [[sim_0 for _ in range(y*2)] for _ in range(y)]

    for j in range(0,len(matrix)-2):
        strMat = matrix[j]
        space = y-j
        for jss in range(space, len(strMat) - space):
            strMat[jss] = sim_1  

    
    for j in range(len(matrix)-2, len(matrix)):
        strMat = matrix[j]
        space = y//2+3
        print(space)
        print(len(strMat) - space)
        for jss in range(space, len(strMat) - space+3):
            print(0)
            strMat[jss-1] = sim_1                  
    return matrix
def gra(matrix: list, sim_1="*",sim_0=" "):
    for Mjs in range(1,len(matrix)-2):
        js = matrix[Mjs]
        for j in range(len(js)):
            if js[j] == sim_1 and js[j-1] == sim_0:
                matrix[Mjs][j] = '/'
            elif js[j] == sim_0 and js[j-1] == sim_1:
                matrix[Mjs][j] = '\\'        
    return matrix
def beautiful(matrix: list,list_toy: list, m=None):
    for j in range(len(matrix[0])):
        if matrix[1][j] == "*":
            matrix[0][j] = "&"            
    if m is None:
        n = randint(a=5, b=len(matrix)*100)
    else:
        n=m
    toys = []
    for _ in range(n+1):
        y = randint(0, len(matrix)-3)
        x = randint(0, len(matrix[0])-1)
        toy = choice(list_toy)       
        if not [y,x] in toys:
            if matrix[y][x] == '*':
        
                matrix[y][x] = toy
                toys.append([y,x])
            else:
                continue
        else:
            continue
    return matrix
            
def printm(matrix:list,seps=' ',ends='\n'):
    print("For Telegram")
    print('```Python')
    for j in matrix:
        print(*j, sep=seps, end=ends)
    print("```")

def write_file(matrix: list, sep=' '):
    with open('tree.txt', 'w') as file:
        file.write("```Python\n")
        for j in matrix:
            file.write(f'{sep}'.join(j))
            file.write('\n')
        file.write('```')

sim_1 = '*' # Из чего ёлочка
sim_0 = ' ' # Пустое пространство
list_toy = list('@#$%&+?') # Игрушки
m = None # кол-во игрушек, при None оно случайно


matrix = tre(10, sim_1=sim_1, sim_0=sim_0) # создание ёлки
matrix = gra(matrix, sim_1=sim_1, sim_0=sim_0) # расстанровка границ
matrix = beautiful(matrix=matrix,  m=120, list_toy=list_toy) # расстановка ёлочных игрушек 
'''write_file(matrix, sep=' ') # если хотите записать результат в файл''' 
printm(matrix, seps=' ')
