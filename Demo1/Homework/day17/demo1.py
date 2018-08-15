'''
建立如下包结构，完成包的使用
	结构：
	1）包名为pkg
	2）一级目录pkg下：
		-- m.py 模块 有函数m_fn
		-- sub1 子包
		-- sub2 子包
	3）二级目录sub1下：
		-- m1.py 模块 有函数 m1_fn
	4）二级目录sub2下：
		-- m2.py 模块 有函数 m2_fn
	要求：
	1）在执行文件run.py只导入pkg包，不做其他导入操作
	2）在执行文件run.py中访问三个函数的方式分别是
		pgk.m_fn()
		pgk.m1_fn()
		pgk.sub2.m2_fn()
	提示：
	1）包pgk与run.py在同级目录
'''
import os, sys
import pkg
pkg.m_fn()
pkg.m1_fn()
pkg.sub2.m2_fn()