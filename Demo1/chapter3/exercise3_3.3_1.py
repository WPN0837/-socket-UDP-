'''
把老文件读进内存
修改字符串
写入新文件
删除老文件
修改新文件名
'''
import sys
import os

num = 0#记录替换次数的计数器
def replace(old = '', new = '', line = ''):
    global num
    if old == new:
        return line
    line_list = line.split(old)
    num += len(line_list) - 1
    return new.join(line_list)

if len(sys.argv) < 4:#命令格式不正确
    print('[old_str new_str file.path]')
else:
    old_str = sys.argv[1]#要被替换的字符串
    new_str = sys.argv[2]#新字符串
    filename = sys.argv[3]#文件名
    new_filename = filename + 'new'#新文件名
    if os.path.isfile(filename):#如果文件存在的情况
        old = open(filename, 'r')
        new = open(new_filename, 'w')
        for line in old:
            if old_str in line:
                line = replace(old_str, new_str, line)
                # line = line.replace(old_str, new_str)#替换字符串
            new.write(line)#把修改后的写进新文件里
        old.close()
        new.close()
        os.remove(filename)
        os.rename(new_filename, filename)
        print('替换了%d处' % (num))
    else:
        print('文件目标不存在！')
