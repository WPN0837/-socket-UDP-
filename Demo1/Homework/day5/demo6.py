l = [5, 2, 1, 4, 3]
# l.sort()
# l = l[::-1]
# print(l)
def func(list):
    for i in range(len(list)-1):
        for j in range(i, len(list) - i - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
print(l)
print(func(l))