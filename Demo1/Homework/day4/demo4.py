'''
求1-2+3-4+5 ... 99的所有数的和
'''
num = 0
for i in range(1, 100):
    if i % 2 == 1:
        num += i
    else:
        num -= i
print(num)