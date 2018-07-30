'''
请写出代码验证 交集 合计 对称差集 差集 子集 父集的效果
'''
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 7, 8, 9}
s3 = {1, 2, 3}
print(s1)
print(s2)
print(s3)
print(s1 & s2, 's1 & s2')
print(s1 | s2, 's1 | s2')
print(s1 ^ s2, 's1 ^ s2')
print(s1 - s2, 's1 - s2')
print(s1 <= s2, 's1 <= s2')
print(s3 <= s1, 's3 <= s1')