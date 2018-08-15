import pickle


class dao:

    def __init__(self, path):
        self.__path = path

    def read(self):
        '''
        读取类型全部数据
        :return:
        '''
        with open(self.__path, 'rb') as file:
            return pickle.load(file)

    def write(self, obj_info):
        '''
        写入全部数据
        :param obj_info:
        :return:
        '''
        with open(self.__path, 'wb') as file:
            pickle.dump(obj_info, file)

    def save(self, obj):
        '''
        保存一个实例对象
        :param obj:
        :return:
        '''
        obj_info = self.read()
        obj_info[obj.id] = obj
        self.write(obj_info)