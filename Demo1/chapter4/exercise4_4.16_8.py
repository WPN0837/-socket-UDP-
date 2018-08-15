import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR, BASE_DIR1)
# os.path.abspath 文件的绝对路径
# os.path.dirname 文件的父目录