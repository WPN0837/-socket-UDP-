'''
编写文件复制工具 输入源文件路径 输入目标文件路径 完成copy
'''
import os
old_file = input('源文件路径：')
new_file = input('复制到(文件夹)：')
if os.path.isfile(old_file):
    if os.path.isdir(new_file):
        if new_file[-1] == '\\' or new_file[-1] == '/':
            new_file += os.path.basename(old_file)
        else:
            new_file += '\\' + os.path.basename(old_file)
        old = open(old_file, 'r', encoding='utf-8')
        new = open(new_file, 'w', encoding='utf-8')
        new.writelines(old.readlines())
        old.close()
        new.close()
    else:
        print('目标文件夹不存在!')
else:
    print('源文件文件不存在！')