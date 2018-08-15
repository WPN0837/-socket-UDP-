import re
resobj = re.compile('[a-z]+.com')
with open('index.html', 'r', encoding='utf-8') as file:
    for line in file:
        res = resobj.findall(line)
        if res:
            print(res)