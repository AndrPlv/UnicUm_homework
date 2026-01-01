r'''
                    &                   
                   /*\                  
                  /$#*\                 
                 /?****\                
                  /***\                 
                 /*****\                
                /*******\               
               /+**#$****\              
                /*$***?*\               
               /*********\              
              /**********?\             
             /********$*&**\            
              /**********#\             
             /****?********\            
            /**%**&******?**\           
           /****************+\          
            /*****#********#\           
           /****?************\          
          /*+********#********\         
         /*$*****?*?***&*******\        
            *****************           
            *****************           
'''

from random import randint,choice

def tree(matrix: list, sim='*'):
    for j in range(len(matrix)-2, len(matrix)):
        strMat = matrix[j]
        space = (len(matrix)-2)//2+3
        for jss in range(space, len(strMat) - space+3):
            strMat[jss-1] = sim
    return matrix     
def tre1(y: int, sim_1="*",sim_0=" "):
    matrix = [[sim_0 for _ in range(y*2)] for _ in range(y+2)]
    for j in range(0,len(matrix)-2):
        strMat = matrix[j]
        space = y-j
        for jss in range(space, len(strMat) - space):
            strMat[jss] = sim_1  
                 
    return matrix
def tre2(y: int, module: int, sim_1="*", sim_0=" "):
    matrix = [[sim_0 for _ in range(y*2)] for _ in range(y+2)]
    hm = y // module 
    step=2
    for modul in range(1, module+1):
        index_end_list = modul * hm
        matrix_for_modul = matrix[index_end_list - hm:index_end_list]
        for j in range(0,len(matrix_for_modul)):
            strMat = matrix_for_modul[j]
            space = y-j - modul*step+2
            for jss in range(space, len(strMat) - space):
                strMat[jss] = sim_1  

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
        AC = len(matrix[0])
        H = len(matrix)
        S = AC*H//2
        mins = int(S * 0.1)
        maxs = int(S * 0.9)
        n = randint(a=mins, b=S)
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
    print("```Python")
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

y = 10 # высота ёлочки
sim_1 = '*' # Из чего состоит ёлочка
sim_0 = ' ' # Пустое пространство
list_toy = list('@#$%&+?') # Игрушки
m = None # кол-во игрушек, при None оно случайно
module = 2 # колл-во "ступениий" в ёлочке

if module == 1:
    matrix = tre1(y=y, sim_1=sim_1, sim_0=sim_0) # создание ёлки
elif module > 1:
    matrix = tre2(y=y, module=module, sim_0=sim_0, sim_1=sim_1) # создание многоступенчатой ёлочки
  
matrix = tree(matrix, sim=sim_1) # ставим ёлку на ножку
matrix = gra(matrix, sim_1=sim_1, sim_0=sim_0) # растанровка границ
matrix = beautiful(matrix, list_toy, m) # расстановка ёлочных игрушек

#write_file(matrix, sep='')
printm(matrix, seps='')
