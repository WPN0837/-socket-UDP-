'''
模拟加密过程
		1）账号密码有用户键盘输入
		2）对得到的账号密码进行md5方式加密处理(采取加盐)
		3）提前建立基本的碰撞测试库
		4）对于用户输入的账号密码进行反馈
			-- 解密成功
			-- 解密失败
'''
md5_list= ['806a6b9f68f9f4c5d1ce0a7084b4cd15', '806a6b9f68f9f4c5d1ce0a7084b4cd15', '2b39c1bd819f0b0fa7af64b349bc1bfd', 'e7eac02270e5f389b6a140607d1abbc6', '87cab3a4264e2186636a4f12e296d157', 'f38a96b6afa45ec7c0033e0185dbcf94', 'e7f4fbf3d8c42802ddfc139789d77f56']
import hashlib
account = input('>>')
password = input('>>')

md5 = hashlib.md5()
md5.update(account.encode('utf-8'))
md5.update(password.encode('utf-8'))
if md5.hexdigest() in md5_list:
    print("解密成功")
else:
    print('解密失败')


# import shelve
# # 序列化
# sl = shelve.open("shelvetest.txt")
# sl["date"] = "8-13"
# sl["list1"] = ["123","456"]
# sl.close()
#
#
# # 反序列化
# s2 = shelve.open("shelvetest.txt")
# print(s2.get("list1"))
# s2.close()


# 语法格式练习: 要求把你的同桌的手机信息用xml来描述

# import xml.etree.ElementTree as et

# 读取xml文档到内存中  得到一个包含所有数据的节点树
# 每一个标签就称之为一个节点 或 元素
# tree = et.parse("text.xml")
# # 获取根标签
# root = tree.getroot()
# # 获取所有的country   找的是第一个
# print(root.find("country"))
# # 找的是所有
# print(root.findall("country"))
#
# # 获取year
# print(root.iter("country"))
# for i in root.iter("country"):
#     print(i)
#
#
# # 遍历整个xml
# for country in root:
#     print(country.tag,country.attrib,country.text)
#     for t in country:
#         print(t.tag, t.attrib, t.text)
#
#
#
# print(root.find("country").get("name"))

# =============================================修改  第所有的country的year文本  改成加1
# 读取到内存
# tree = et.parse("text.xml")
# for country in tree.findall("country"):
#     # yeartag = country.find("year")
#     # yeartag.text = str(int(yeartag.text) + 1)   修改标签文本
#
#     # country.remove(country.find("year"))     删除标签
#
#     # 添加子标签
#     newtag = et.Element("newTag")
#     # 文本
#     newtag.text = "123"
#     #属性
#     newtag.attrib["name"] = "DSB"
#     #添加
#     country.append(newtag)

# 写回到内存
# tree.write("text.xml",encoding="utf-8",xml_declaration=False)

# import configparser
# conf = configparser.ConfigParser()
# conf.read('config.ini', encoding='utf-8')
# print(conf['sections']['options'])
# conf['sections']['options'] = 'new_config'
#
# conf.write(open('config.ini', 'w', encoding='utf-8'))