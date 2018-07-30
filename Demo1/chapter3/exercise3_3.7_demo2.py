'''
用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
'''
import os

num = 0#记录替换次数的计数器
def replace(old = '', new = '', line = ''):
    global num
    if old == new:
        return line
    line_list = line.split(old)
    num += len(line_list) - 1
    return new.join(line_list)

def moditfy(*argv):
    old_str = argv[0]#要被替换的字符串
    new_str = argv[1]#新字符串
    filename = argv[2]#文件名
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

if __name__ == '__main__':
    moditfy('1', '2', 'C:/Users/WPN/PycharmProjects/Demo1/chapter3/a.txt')