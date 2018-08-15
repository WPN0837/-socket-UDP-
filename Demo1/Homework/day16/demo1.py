'''
掌握课堂案例：验证码
'''
import random
def make_Verification_code():
    # chr(random.randint(65, 90)), str(random.randint(0, 9))
    l = [chr(random.randint(65, 90)) for i in range(6)]
    return ''.join(l)
print(make_Verification_code())