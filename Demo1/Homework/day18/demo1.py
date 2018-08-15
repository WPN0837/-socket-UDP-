'''
借助shelve模块，完成将数据
		"week": ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
		"person": {"name": "Zero", "age": 8, "height": 180}
		序列化到date.shl文件中
		并反序列化来测试文件中的数据：如访问数据	"Tues"及"Zero"
	探索：
		自定义一个有打印语句的简单函数，将函数序列化到文件中，在反序列化测试函数中的打印语句
'''
import shelve
dic = {"week": ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"],
		"person": {"name": "Zero", "age": 8, "height": 180}}
f = shelve.open('date.shl')
f["week"] = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
f["person"] = {"name": "Zero", "age": 8, "height": 180}
f.close()

f = shelve.open('date.shl')
print(f['week'])
f.close()

def func(data):
    f = shelve.open('date.shl')
    f['data'] = data
    f.close()
def func1():
    f = shelve.open('date.shl')
    print(f['data'])
    f.close()