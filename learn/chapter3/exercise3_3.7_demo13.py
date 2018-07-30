portfolie = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
def f(dic):
    if dic['price'] > 100.0:
        return True
    else:
        return False
num = 0
for i in portfolie:
    num += i['shares'] * i['price']
print(num)
for i in filter(f, portfolie):
    print (i)