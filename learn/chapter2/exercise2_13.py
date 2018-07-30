l1 = [11, 22, 33]
l2 = [22, 33, 44]
s1 = set(l1)
s2 = set(l2)
print(list(s1 & s2))
print(list(s1 - s2))
print(list(s2 - s1))
print(list(s1 ^ s2))