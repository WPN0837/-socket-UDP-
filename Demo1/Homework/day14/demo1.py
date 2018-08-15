'''
定义一个cuboid模块，模块中有三个变量长(long)宽(wide)高(high)，数值自定义，有一个返回值为周长的perimeter方法，一个返回值为表面积的area方法
'''
long = 1
width = 2
high = 3

def getarea():
    return (long * width + long * high + high * width) * 2

def getperimeter():
    return (long + width + high) * 4