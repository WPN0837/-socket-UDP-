'''
例如 北京市 省会：直辖市 面积：XX  人口：XX  ，浙江省： 省会：杭州市  面积：XX 人口：XX
		最后取出北京市按以下格式打印
				========= 北京 ========
				省会：直辖市
				面积：xxx
				人口：xxx
				========= end ========
'''
c = {
    '北京市': {
        '省会': '直辖市',
        '面积': 'XX',
        '人口': 'XX'
    },
    '浙江省': {
        '省会': '杭州市',
        '面积': 'XX',
        '人口': 'XX'
    }
}
def show(c):
    for key, value in c.items():
        print(key, value)

for key, value in c.items():
    print('========= %s ========' % (key))
    show(value)
print('========== end =========')