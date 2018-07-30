li = ['alex', 'eric', 'rain']

print(len(li))

li.append('seven')
print(li)

li = ['alex', 'eric', 'rain']
li.insert(0, 'Tony')
print(li)

li = ['alex', 'eric', 'rain']
li[1] = 'Kelly'
print(li)

li = ['alex', 'eric', 'rain']
li.remove('eric')
print(li)

li = ['alex', 'eric', 'rain']
print(li.pop(1))
print(li)

li = ['alex', 'eric', 'rain']
li.pop(2)
print(li)

li = ['alex', 'eric', 'rain']
for i in range(len(li)-1, -1, -1):
    if i == 1 or i == 2 or i == 3:
        li.pop(i)

li = ['alex', 'eric', 'rain']
print(li[::-1])

li = ['alex', 'eric', 'rain']
for i in range(len(li)):
    print(i)

li = ['alex', 'eric', 'rain']
for enum, value in enumerate(li):
    print(enum+100, value)

li = ['alex', 'eric', 'rain']
for l in li:
    print(l)
