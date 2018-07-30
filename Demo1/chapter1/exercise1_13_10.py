import random
name=[]
address=[]
something=[]
while True:
    name1=input('请输入姓名，只输入空格结束输入')
    if(name1 != " "):
        name.append(name1)
    else:
        break

while True:
    address1=input('请输入地方，只输入空格结束输入')
    if(address1 != " "):
        address.append(address1)
    else:
        break

while True:
    something1=input('请输入事情，只输入空格结束输入')
    if(something1 != " "):
        something.append(something1)
    else:
        break

msg='''敬爱的可爱的%s，最喜欢在%s地方干%s'''%(random.choice(name),random.choice(address),random.choice(something))
print(msg)