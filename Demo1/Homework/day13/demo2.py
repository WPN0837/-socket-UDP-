'''
文件shopping.txt内容如下
		mac,2000,3
		lenovo,3000,10
		tesla,1000000,10
		chicken,200,1

		求总共花了多少钱？
		打印出所有的商品信息，格式为
		[{'name':'xxx','price':'3333','count':3},....]
		求单价大于10000的商品信息，格式同上
'''
info_list = []
name_list = ['name', 'price', 'count']
with open('shopping.txt', 'r', encoding='utf-8') as info:
    for line in info:
        info_list.append(dict(zip(name_list, line.strip('\n').split(','))))
num = 0
for i in info_list:
    num += int(i['price']) * int(i['count'])
print(num)
print(info_list)