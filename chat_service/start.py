import os
import sys

sys.path.append(os.path.dirname(__file__))

from threading import Thread
from bin import service
from interface import service_interface

if __name__ == '__main__':
    t1 = Thread(target=service_interface.detect_session)
    t2 = Thread(target=service_interface.delete_session)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    service.run()