tu = ('alex', 'eric', 'rain')
print(len(tu))
print(tu[1])
print(tu[0], tu[1])
for i in range(len(tu)):
    print(tu[i])
for t, value in enumerate(tu):
    print(t+10, value)