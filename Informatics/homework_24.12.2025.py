operat = {'+': lambda a,b: a+b,
          '-': lambda a,b: a-b,
          '*': lambda a,b: a*b,
          '**': lambda a,b: a**b,
          '/': lambda a,b: a/b,
          '//': lambda a,b: a//b,
          '%': lambda  a,b: a%b}

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
