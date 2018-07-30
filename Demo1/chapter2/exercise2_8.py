s = 'alex'
print(list(s))
print(tuple(s))
li = ['alex', 'seven']
print(tuple(li))
tu = ('alex', 'seven')
print(list(tu))
l = range(10, 10+len(li))
print(dict(zip(l, li)))