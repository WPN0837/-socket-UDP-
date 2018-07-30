num = [1, 3, 5, 6, 7, 8]
def f(n):
    if n % 2 == 0:
        return True

    else:
        return False
for i in filter(f, num):
    print(i)