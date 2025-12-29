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
        for jss in range(space, len(strMat) - space):
            strMat[jss] = sim_1                  
    return matrix
def gra(matrix: list):
    for Mjs in range(1,len(matrix)-2):
        js = matrix[Mjs]
        for j in range(len(js)):
            if js[j] == '*' and js[j-1] == ' ':
                matrix[Mjs][j] = '/'
            elif js[j] == ' ' and js[j-1] == '*':
                matrix[Mjs][j] = '\\'        
    return matrix
def beautiful(matrix: list):
    for j in range(len(matrix[0])):
        if matrix[1][j] == "*":
            matrix[0][j] = "&"            
    n = randint(a=5, b=len(matrix)*100)
    toys = []
    list_toy = list('@#$%&+?')
    for _ in range(n):
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
    print('```')
    for j in matrix:
        print(*j, sep=seps, end=ends)
    print("```")
def write_file(matrix: list):
    with open('tree.txt', 'w') as file:
        file.write("```\n")
        for j in matrix:
            file.write(' '.join(j))
            file.write('\n')
        file.write('```')
matrix = tre(15)
matrix = gra(matrix)
matrix = beautiful(matrix)
#write_file(matrix)
printm(matrix)
