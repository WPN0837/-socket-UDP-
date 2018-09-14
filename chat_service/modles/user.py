from db import db_handle


class user:
    account = None
    password = None
    friends = []

    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.friends = []

    @classmethod
    def register(cls, account, password):
        obj = cls(account, password)
        obj.save()

    def get_friends(self):
        return self.friends

    def add_friend(self, account):
        self.friends.append(account)
        self.save()

    def delete_friend(self, account):
        self.friends.remove(account)
        self.save()

    def save(self):
        db_handle.save(self)

    @classmethod
    def get_user_by_account(cls, account):
        return db_handle.get_user(account)
