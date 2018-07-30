'''
数据结构
1,Alex Li,22,13651024608,IT,2013-04-01

'''
# import time
info = {}
staff_id = 0
def add(list = []):
    global staff_id
    global info
    _id = str(staff_id + 1)
    # enroll_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # list = [_id, name, age, phone, dept, enroll_date]
    list.insert(0, _id)
    info[_id] = list
    with open('info3', 'a', encoding='utf-8')as all_info:
        all_info.write(','.join(list) + '\n')
        all_info.flush()
    staff_id += 1


def delete(_id):
    if str(_id) in info:
        info.pop(str(_id))
    flush()


def update(list = [], args = []):
    template = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    global info
    t1 = template.index(args[0])
    t2 = template.index(list[0])
    for value in info.values():
        if value[t1] == args[1]:
            value[t2] = list[1]
    flush()


def find(list = [], args = []):
    '''
    find name,age from staff_table where age > 22
    find * from staff_table where dept = 'IT'
    find * from staff_table where enroll like '2013'
    :return:
    '''
    template = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    result = {}
    #>
    def d():
        t = template.index(args[0])
        for i, value in info.items():
            if value[t] > args[2]:
                result[i] = value
        return result

    #<
    def x():
        t = template.index(args[0])
        for i, value in info.items():
            if value[t] < args[2]:
                result[i] = value
        return result

    #=
    def equal():
        t = template.index(args[0])
        for i, value in info.items():
            if value[t] == args[2]:
                result[i] = value
        return result

    #like
    def like():
        t = template.index(args[0])
        for i, value in info.items():
            if args[2] in value[t]:
                result[i] = value
        return result
    if args[1] == '>':
        result = d()
    elif args[1] == '<':
        result = x()
    elif args[1] == '=':
        result = equal()
    elif args[1] == 'like':
        result = like()
    else:
        print('查询错误！')
    if len(list) == 0:
        show(result)
    else:
        result1 = {}
        for i, value in result.items():
            value1 = []
            for j in list:
                value1.append(value[template.index(j)])
            result1[i] = value1
        show(result1)

#显示数据
def show(info = {}):
    for i in info.values():
        for j in i:
            print(j, end=' ')
        print()
        # print('%s %s %s %s %s %s' % (i[0], i[1], i[2], i[3], i[4], i[5]), end='')

#把内存中的数据写到硬盘
def flush():
    with open('info3', 'w', encoding='utf-8')as all_info:
        for i in info.values():
            all_info.write(','.join(i))
        all_info.flush()

if __name__ == '__main__':
    with open('info3', 'r', encoding='utf-8')as all_info:
        lines = all_info.readlines()
        for line in lines:
            line_list = line.split(',')
            info[line_list[0]] = line_list
            staff_id = int(line_list[0])
    show(info)
    while True:
        cmd = input('>>:')
        if cmd.startswith('find'):
            #find name,age from staff_table where age > 22
            #cmd.split()[1].split(',')  cmd.split()[5:8]
            find(cmd.split()[1].split(','), cmd.split()[5:8])
        elif cmd.startswith('add'):
            #add table Alex Li,25,134435344,IT,2015-10-29
            # ' '.join(cmd.split()[2:]).split(',')
            add(' '.join(cmd.split()[2:]).split(','))
        elif cmd.startswith('del'):
            #del from table where id = 3
            # cmd.split()[-1]
            delete(cmd.split()[-1])
        elif cmd.startswith('update'):
            #update tabele set dept = 'Market' where dept = 'IT'
            list = cmd.split()
            update([list[3], list[5]], [list[-3], list[-1]])
        elif cmd == 'show':
            show(info)
        elif cmd == 'quit':
            break
        else:
            print('%s 命令错误！' % cmd)