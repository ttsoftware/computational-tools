import sqlite3


class SQLite(object):
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.conn.text_factory = str

    def get_table_names(self):
        c = self.conn.cursor()
        tables = c.execute("SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        self.conn.close()

        return map(lambda x: x[2], tables)

    def find_all(self, table):
        c = self.conn.cursor()
        data = c.execute("SELECT * FROM " + table + ";").fetchall()
        self.conn.close()

        return data

    def find_by(self, table, attr, val):
        c = self.conn.cursor()
        data = c.execute("SELECT * FROM " + table + " WHERE " + attr + "='" + val + "';").fetchall()
        self.conn.close()

        return data

    def query(self, q):
        c = self.conn.cursor()
        data = c.execute(q).fetchall()
        self.conn.close()

        return data
