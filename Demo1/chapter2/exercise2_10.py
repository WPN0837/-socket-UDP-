li = ['手机', '电脑', '鼠标垫', '游艇']
while True:
    print(
        '''
        0.退出
        1.输入序号，显示商品
        2.添加商品
        '''
    )
    c = int(input('请选择功能:'))
    if c == 0:
        break
    elif c == 1:
        n = int(input('请选择商品序号:'))
        if n <= 0 or n > len(li):
            print('超出范围！')
        else:
            print(li[n-1])
    elif c == 2:
        s = input('请输入商品名称：')
        li.append(s)
    else:
        print('选择的功能不存在~~~')
