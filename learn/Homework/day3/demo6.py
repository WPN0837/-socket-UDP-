'''
设计程序实现如下功能，要求用户输入两个数 加减乘除 可使用四个文件每个文件完成一种运算 或使用if
'''
m = input()
a = 0
b = 0
c = ''
falg = False

for i in m:
    if ord(i) >= ord('0') and ord(i) <= ord('9'):
        if falg:
            b = b * 10 + ord(i) - ord('0')
        else:
            a = a * 10 + ord(i) - ord('0')
    else:
        falg = True
        c = i
if c == '+':
    print(a+b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('运算符号错误！')

