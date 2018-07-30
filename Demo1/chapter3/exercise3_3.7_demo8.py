def f(i):
    if i == 1 or i == 0:
        return 1
    else:
        return f(i-1) * i
if __name__ == '__main__':
    print(f(5))