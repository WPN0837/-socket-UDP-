'''
使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
'''
def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)
print(F(6))