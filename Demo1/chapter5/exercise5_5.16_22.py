import json
import time
info = {
    'egon': {'password': '123', 'status': False, 'timeout': 0},
    'alex': {'password': '456', 'status': False, 'timeout': 0}
}
def write():
    with open('22.json', 'w') as info_file:
        json.dump(info, info_file)
def read():
    with open('22.json', 'r') as info_file:
        info_data = json.load(info_file)
    print(info_data, type(info_data))
class customer:
    def __init__(self, name , password, status = False, timeout = 0):
        self.name = name
        self.password = password
        self.status = status
        self.timeout = timeout
    @property
    def db(self):
        return self.__dict__
    def login(self):
        if self.status:
            return
        count = 0
        while True:
            name = input('用户名:')
            password = input('密码：')
            if name == self.name:
                if password == self.password:
                    if time.time() - self.timeout >= 10:
                        self.status = True
                        return
                    else:
                        print('%s秒后再登录' % (self.timeout + 10 - time.time()))
                        continue
                else:
                    count += 1
                    if count >= 3:
                        self.timeout = time.time()
            print('用户名或密码错误')
c = customer('egon', '123')
# print(c.db())
c.login()