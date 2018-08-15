import sys, os
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from core import run
if __name__ == '__main__':
    run.run()