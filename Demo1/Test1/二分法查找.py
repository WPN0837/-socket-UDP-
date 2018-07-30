'''
二分法查找
传进方法内的列表必须是已经排序好的,本方法按升序排列
本例查找返回元素的下标
'''
def find_by_dichotomy(list, num):
    if len(list) == 1:
        if list[0] == num:
            print(list[0])
        else:
            print('查找的信息不存在')
        return None
    else:
        if list[len(list)//2] == num:
            print(list[len(list)//2])
            return None
        elif list[len(list)//2] > num:
            find_by_dichotomy(list[:len(list)//2], num)
        else:
            find_by_dichotomy(list[len(list) // 2:], num)

list = [5, 7, 8, 6, 9, 4, 3, 2, 1]
# list = sorted(list)
list.sort()
print(list)
find_by_dichotomy(list, 5)