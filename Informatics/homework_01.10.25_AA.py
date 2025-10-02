print('Script:')
data = input('>>> ')
print(data.replace(chr(160), ' ', data.count(chr(160))))
