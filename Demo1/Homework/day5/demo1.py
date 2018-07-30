l = list()
num = 0.0
for i in range(5):
    c = int(input('%d:' % (i+1)))
    num += c
    l.append(c)
l.sort()

print(str(l[0]), str(l[4]), str(num/5))