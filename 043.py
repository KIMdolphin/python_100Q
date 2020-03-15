num = int(input())
bi = ""
while num > 1:
    if num % 2 == 0:
        bi = "0" + bi
    else:
        bi = "1" + bi
    num = num//2
    
if num == 1:
    bi = "1" + bi
if num == 0:
    bi = "0" + bi
    
print(bi)
