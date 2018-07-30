'''
有如下字符串("language,is,perfect,hello,i am jack,python")
		编写代码 将其修改为"hello i am jack python is perfect language" 字符串
'''
s = 'language,is,perfect,hello,i am jack,python'
l = s.split(',')
l[0], l[1], l[2], l[3], l[4], l[5] = l[3], l[4], l[5], l[1], l[2], l[0]
s = ' '.join(l)
print(s)