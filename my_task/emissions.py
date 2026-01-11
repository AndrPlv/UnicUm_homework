#[2,3,4,5,6,7,-10,10] False
#[1,2,3,4,5,6,7,8,9,10] True
def no_up(data:list):
    steps = sum(data) / len(data)  
    for j in range(2,len(data)+1):
        micro = sum(data[j-2:j]) / len(data[j-2:j])
        if micro-steps < data[j-1] < micro+steps:
            pass
        else:
            return f'Status: False. Index {j-1} and value {data[j-1]} (arithmetic mean {micro})'
    else:
        return 'Status True'
s = [1,2,3,4,5,6,7,8,9,10]
out = no_up()
print(out)
