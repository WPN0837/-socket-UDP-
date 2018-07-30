'''
	使用函数完成以下功能,数据格式如下
	[
		{"name":"张无忌","number","sh01","math":90,"english":87,"chinese":56},
		{"name":"武则天","number","sh02","math":40,"english":97,"chinese":67}....

	]
	提供以下功能函数
		获取指定学生的成绩
		获取指定学号的成绩
		根据学生的学号修改姓名
		根据姓名修改指定学科的成绩
		删除指定学生及其成绩
'''
li = [{"name": "张无忌", "number": "sh01", "math": 90, "english": 87, "chinese": 56},
      {"name": "武则天", "number": "sh02", "math": 40, "english": 97, "chinese": 67}
      ]
def get_score_by_name(name):
    for i in li:
        if name == i['name']:
            print('"math": %s, "english": %s, "chinese": %s' % (i["math"], i["english"], i["chinese"]))
            return {"math": i['math'], "english": i["english"], "chinese": i["chinese"]}
            break
def get_score_by_number(number):
    for i in li:
        if number == i['number']:
            print('"math": %s, "english": %s, "chinese": %s' % (i["math"], i["english"], i["chinese"]))
            break
def change_name_by_number(number, name, li):
    for i in range(len(li)):
        if li[i]['number'] == number:
            li[i]['name'] = name
            return li
def change_score_by_name(subject, score, name, li):
    for i in li:
        if name == i['name']:
            i[subject] = score
            return li
def delete_by_name(name):
    for i in li:
        if i['name'] == name:
            li.remove(i)
            return li
if __name__ == '__main__':
    get_score_by_name('张无忌')
    get_score_by_number('sh01')
    li = change_name_by_number('sh01', '周芷若', li)
    li = change_score_by_name('math', 100, '周芷若', li)
    print(li)