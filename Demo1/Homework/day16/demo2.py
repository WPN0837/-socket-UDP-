'''
掌握课堂案例：进度条
'''
import time
p=0.0
def func(m):
    print('\r%s>%s%.2f%%' % ('='*int(100*m), ' '*int(100*(1-m)), m*100), end='')
for i in range(100):
    time.sleep(0.5)
    p += i/100.0
    func(p) if p <= 1 else func(1.0)
    if p > 1:break