import math as m
num = 0
for i in range(2, 101):
    for j in range(2, int(m.sqrt(i))+1):
        if i % j == 0:
            falg = False
            break
    else:
        num += i
print(num)