def v(username, password):
    with open('info', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if username in line:
                if password in line:
                    num = line.split('|count:')[1].split('|')[0]
                    if int(num) >= 3:
                        lines[i] = line.replace('|count:%s|' % num, '|count:%s|' % str(int(num)+1))
                        f.seek(0, 0)
                        f.writelines(lines)
                        return 4
                    lines[i] = line.replace(num, str(0))
                    f.seek(0, 0)
                    f.writelines(lines)
                    return -2
                else:
                    num = line.split('|count:')[1].split('|')[0]
                    old = '|count:%s|' % (num)
                    new = '|count:%s|' % (str(int(num)+1))
                    lines[i] = line.replace(old, new)
                    f.seek(0, 0)
                    f.writelines(lines)
                    return int(num)
            else:
                return -1

if __name__ == '__main__':
    while True:
        name = input('用户名:')
        password = input('密码:')
        username = '|name:%s|' % (name)
        pwd = '|password:%s|' % (password)
        falg = v(username, pwd)
        if falg == -1:
            print('用户名不存在！')
        elif falg >= 3:
            print('该用户已经被锁定！')
        elif falg == -2:
            print('登录成功！')
        else:
            print('密码错误！')