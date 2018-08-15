'''
现有一个text目录下有a.txt,b.txt,c.py三个文件，利用subprocess模块，将三个文件的文件名存放到tag.txt文件中
	思考：执行文件在text目录下与不在text目录下两种情况
'''
import os
path = os.path.dirname(__file__)
res = os.walk(path + '/text')
res1 =next(res)
with open('tag.txt', 'w', encoding='utf-8') as file:
    for i in res1[2]:
        file.write(str(i)+'\n')