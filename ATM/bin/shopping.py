#商城购物用户信息文件 shopping_customer_db
from ATM.core import operating_log
from ATM.core import shopping_controller as C
from ATM.core import shopping_operating as O
from ATM.core import shopping_commodity_operating as OC
log = operating_log.logger('../log/shopping.log')
log.send(None)
session = {}
user_state = {}
if __name__ == '__main__':
    while True:
        print(
    '''
    0.查看所有商品
    1.购买
    2.查看购物车
    3.查看已购买商品''')
        if len(session) == 0:
            print('\t4.登录\n\t5.注册\n\t6.')
        cmd = input('>>')
        if cmd == '0':
            C.show()
        elif cmd == '1':
            _id = input('选择商品编号:')
            if len(OC.search_buyed([_id])) < 1:
                print('该商品不存在！')
                continue
            C.add_cart(_id, session)
            if len(session) != 0:
                session = O.search(session['name'])[0]
        elif cmd == '2':
            C.cart(session)
        elif cmd == '3':
            C.show_buyed(session)
        elif cmd == '4':
            if len(session) != 0:
                print('命令错误！')
                continue
            session = C.login_interface()
        elif cmd == '5':
            if len(session) != 0:
                print('命令错误！')
                continue
            C.register()
        elif cmd == 'quit':
            break
        else:
            print('命令错误！')