def plus(a:int,b:int): return  a+b
def minus(a:int,b:int): return  a-b
def mult(a:int,b:int): return a*b
def degree(a:int,b:int): return a**b
def dele1(a:int,b:int): return a/b
def dele2(a:int,b:int): return a//b
def dele3(a:int,b:int): return a%b


operat = {'+': plus,
          '-': minus,
          '*': mult,
          '**': degree,
          '/': dele1,
          '//': dele2,
          '%': dele3}

def main(operat: dict):
    print('Число a:')
    a = int(input(">>> "))
    print('Число b:')
    b = int(input(">>> "))    
    print('Операция:')
    op = input(">>> ")
    return operat[op](a,b)

result = main(operat)
print(f'>>> {result}')
