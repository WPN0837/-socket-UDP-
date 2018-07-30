
# list = [3,1,2,4,6,5,4,9,4,1,3,2]
# list = [1,2,4,3,6,5]
# print(list)
# for i in range(len(list) - 1):
#     for j in range(len(list)- 1):
#         if list[j+1] < list[j]:
#             list[j+1], list[j] = list[j], list[j+1]
# print(list)
# def func(list):#冒泡排序
#     for i in range(len(list)-1):
#         for j in range(len(list) - i - 1):
#             if list[j] < list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     return list
# list = func(list)
# print(list)
# def func1(list):#选择排序
#     for i in range(len(list) -1 ):
#         for j in range(i+1,len(list)):
#             if list[i] < list[j]:
#                 list[i], list[j] =  list[j], list[i]
#     return list
# func1(list)
# print(list)

# import random
# list = []
# for i in range(10):
#     list.append(random.randint(0, 100))
# ## 快速排序
# def func2(list):#递增
#     if len(list) <= 1:
#         return list
#     i = 0
#     j = len(list)
#     while True:
#         for i in range(i, len(list)):#从左向右
#             if list[i] > list[0]:
#                 break
#         for j in range(0, j)[::-1]:#从右向左
#             if list[j] < list[0]:
#                 break
#         if i >= j:
#             break
#         list[i], list[j] = list[j], list[i]
#     list[j], list[0] = list[0], list[j]
#     list[0:j] = func2(list[0:j])
#     list[j + 1:len(list)] = func2(list[j + 1:len(list)])
#     return list
# print(list)
# print(func2(list))



# with open('a.txt', 'a', encoding='utf-8')as f:
#     for i in range(10):
#         f.write(str(list)+'\n')