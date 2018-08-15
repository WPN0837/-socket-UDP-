'''
文件内容如下,标题为:姓名,性别,年纪,薪资
		egon male 18 3000
		alex male 38 30000
		wupeiqi female 28 20000
		yuanhao female 28 10000

		要求:
		从文件中取出每一条记录放入列表中,
		列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
'''
info_list = []
name_list = ['name', 'sex', 'age', 'salary']
with open('test.txt', 'r', encoding='utf-8') as info:
    for line in info:
        info_list.append(dict(zip(name_list, line.strip('\n').split(' '))))
print(info_list)