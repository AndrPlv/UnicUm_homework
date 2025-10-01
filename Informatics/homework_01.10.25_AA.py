code = f''' ''' # необработанный код
inp = 160 # который заменять
out = ' ' # которым заменить
for j in code:
    if ord(j) == inp:
        code = code.replace(j, out)
    else:
        pass
print(code) 
