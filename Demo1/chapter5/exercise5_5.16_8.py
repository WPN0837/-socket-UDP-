import pymysql
class exc:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
    def exc1(self, sql):
        conn = pymysql.connect(self.host, self.port, self.db, self.charset)
        return conn.execute(sql)
    def exc2(self, sql):
        conn = pymysql.connect(self.host, self.port, self.db, self.charset, self.proc_name)
        return conn.call_proc(sql)

