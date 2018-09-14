class user:
    account = None
    password = None
    friends = []

    def __init__(self, account, password, friends):
        self.account = account
        self.password = password
        self.friends = friends

    def get_friends(self):
        return self.friends

    def add_friend(self, account):
        self.friends.append(account)

    def delete_friend(self, account):
        self.friends.remove(account)
