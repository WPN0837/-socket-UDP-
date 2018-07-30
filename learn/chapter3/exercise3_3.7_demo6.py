def v(*args):
    max = args[0]
    min = args[0]
    for i in args:
        if max < int(i):
            max = int(i)
        if min > int(i):
            min = int(i)
    return {'max': max, 'min': min}
if __name__ == '__main__':
    print(v(1,2,3,4,5))