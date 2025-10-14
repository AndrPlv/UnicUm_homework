from random import randint as rd
print("Введите размеры матрицы в формате: X:Y")
matrix_size = input(">>> ").split(':')
matrix_size_X = int(matrix_size[0])
matrix_size_Y = int(matrix_size[1])
print('Количество островов:')
room = int(input(">>> "))
print('Максимальное количество клеток которой может быть в острове:')
max_len_room = int(input(">>> "))


matrix_main = [['O' for _ in range(matrix_size_X)] for _ in range(matrix_size_Y)]
# (y == 0 or x == 0) or (y == matrix_size_Y - 1 or x == matrix_size_X - 1)

C_list_codent_room = [(rd(1, matrix_size_Y-1), rd(1, matrix_size_X-1))]
for _ in range(room):
    R = 5
    while (True): 
        c_x = rd(1, matrix_size_X-1)
        c_y = rd(1, matrix_size_Y-1)
        if C_list_codent_room[-1][0] - c_x == R or C_list_codent_room[-1][0] - c_y == R:
            C_list_codent_room.append((c_y,c_x))
            break
#for _ in range(room):
#    for _ in range(rd(3, max_len_room)):
#        while(True):
#            pass
for obj in C_list_codent_room:
    matrix_main[obj[0]][obj[1]] = 'X'
for ele in matrix_main:
    print(*ele)
