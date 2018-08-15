'''
5.现有一个run.py运行文件，与run文件同级目录下有一个pgk文件夹，文件夹下有两个模块m1、m2，m1模块内有功能f1，可以打印字符串"我是m1模块"，m2模块内有功能f2，
可以打印字符串"我是m2模块"，在run文件中，通过绝对路径方式导入m1模块，验证功能，通过相对路径导入m2模块，验证功能，在模块m1中通过相对路径导入m2模块，验证功能
'''
import sys
from Demo1.Homework.day15.pgk import m1
from pgk import m2
m1.f1()
m2.f2()
print(sys.path)