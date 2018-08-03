'''
文件shopping.txt内容如下

		mac,20000,3
		lenovo,3000,10
		tesla,1000000,10
		chicken,200,1
		求总共花了多少钱？

	打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]

	求单价大于10000的商品信息,格式同上
'''
def read():
    t = ['name', 'price', 'count']
    l = []
    with open('shopping.txt', 'r', encoding='utf-8')as s:
        for i in s.readlines():
            dic = dict(zip(t, i.strip('\n').split(',')))
            l.append(dic)
    return l
if __name__ == '__main__':
    l = read()
    print(l)
    print(sum([int(i['price']) * int(i['count']) for i in l]))
    f = filter(lambda i: True if int(i['price'])>10000 else False,l)
    for i in f:
        print(i)
    print(max(l, key=lambda i: int(i['price'])))