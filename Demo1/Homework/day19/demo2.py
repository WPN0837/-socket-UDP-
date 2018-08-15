'''
遍历book.xml文件，通过正则匹配，将所有书名存放到book.txt文件中
'''
import xml.etree.ElementTree as ET
# tree = ET.parse('book.xml')
# root = tree.getroot()
# for node in root:
#     print(node.text)
with open('book.xml','r', encoding='utf-8') as file:
    lines = file.readlines()
import re
t = '<Book>(.+)</Book>'
reobj = re.compile(t)
result = []
for line in lines:
    res = reobj.findall(line)
    if res:
        result.append(res[0])
with open('book.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(result))