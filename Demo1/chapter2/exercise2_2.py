li = ['alec', ' aric', 'Alex', 'Tony', 'rain']
tu = ('alec', ' aric', 'Alex', 'Tony', 'rain')
dic = {'k1': 'alec', 'k2': ' aric', 'k3': 'Alex', 'k4': 'Tony'}

for l in range(0, len(li)):
    s = li[l].strip()
    li[l] = s
    if (s[0] == 'a' or s[0] == 'A') and s[-1] == 'c':
        print(s)
print(li)
for t in range(0, len(tu)):
    s = tu[t].strip()
    tu = tu[: t] + (s,) + tu[t + 1:]
    if (s[0] == 'a' or s[0] == 'A') and s[-1] == 'c':
        print(s)
print(tu)
for d in dic.items():
    key, value = d
    s = value.strip()
    dic[key] = s
    if (s[0] == 'a' or s[0] == 'A') and s[-1] == 'c':
        print(key + ':' + s)
print(dic)