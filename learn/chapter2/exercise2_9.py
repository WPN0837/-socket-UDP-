s = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
k1 = []
k2 = []
d = {}
for i in s:
    if i < 66:
        k2.append(i)
    elif i>66:
        k1.append(i)
d['k1'] = k1
d['k2'] = k2
print(d)
