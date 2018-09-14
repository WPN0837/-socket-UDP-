import os
import pickle
from conf import settings


def save(obj):
    path_dir = os.path.join(settings.DB_DIR, obj.__class__.__name__)
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    path_file = os.path.join(path_dir, obj.account)
    with open(path_file, 'wb') as file:
        pickle.dump(obj, file)


def get_user(account):
    path_dir = os.path.join(settings.DB_DIR, 'user')
    path_file = os.path.join(path_dir, account)
    if not os.path.exists(path_file):
        return None
    with open(path_file, 'rb') as file:
        return pickle.load(file)
