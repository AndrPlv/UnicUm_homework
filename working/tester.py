import os
import sys
from time import sleep
matrix = [[0 for _ in range(10)] for _ in range(10)]

def clear_console():
    clear = {'linux': 'clear', 'win32': 'cls'}
    os.system(clear[sys.platform])
for j in range(10+1):
    for y in range(10):
        for x in range(10):
            matrix[y][x] += 1
    clear_console()
    sleep(0.5)
    for j in matrix:
        print(*j, sep=' ')
    sleep(1)