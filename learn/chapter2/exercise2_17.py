li = [1, 3, 2, 7, 6, 23, 41, 24, 33, 85, 56]
i = 0
for i in range(len(li)-1-i):
    for j in range(i+1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)