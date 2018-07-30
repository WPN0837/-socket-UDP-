c = int(input())
for i in range(1, c+1):
    s = ''
    s += '*' * (i-1) + ' ' * (c-i)
    print(s[::-1], '*', s, sep='')