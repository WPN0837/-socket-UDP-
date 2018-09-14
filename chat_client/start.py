import os, sys
from threading import Thread

sys.path.append(os.path.dirname(__file__))
from bin import client

if __name__ == '__main__':
    t1 = Thread(target=client.recv_chat)
    t2 = Thread(target=client.conn_session)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    client.run()