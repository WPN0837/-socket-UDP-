def V(dic):
    dic1 = {}
    for key in dic:
        if len(dic[key]) > 2:
            dic1[key] = dic[key][:2]
        else:
            dic1[key] = dic[key]
    return dic1
if __name__ == '__main__':
    dic = {1: '123', 2: '12', 3: '1'}
    print(V(dic))
    print(dic)