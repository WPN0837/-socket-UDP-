'''
为题目五编写装饰器，实现缓存网页内容的功能：
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
'''
url_list = []
import requests
def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        res = None
        if len(args) > 0 and args[0] in url_list:
            print('%s已存在' % args[0])
        else:
            res = func(*args, **kwargs)
            url_list.append(args[0])
        return res
    return wrapper
@zhuangshiqi
def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        # with open(url, 'w', encoding='utf-8')as file:
        #     file.write(response.text)
        return response.text
while True:
    url = input('url:')
    get(url)
    print(url_list)