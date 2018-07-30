'''
有以下列表
		["python","java","C++","PHP","HTML","python","C++","Ruby"]
		编写代码去除列表中重复的元素
'''
l = ["python", "java", "C++", "PHP", "HTML", "python", "C++", "Ruby"]
print(list(set(l)))