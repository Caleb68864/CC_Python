import sqlite3


class CCFile:
    def __init__(self, database):
        self.database = database
        self.conn = ""

    def connect(self):
        self.conn = sqlite3.connect(self.database, check_same_thread=False)

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def executesql(self, sql):
        cursor = self.conn.cursor()
        while True:
            try:
                cursor.execute(sql)
                return cursor
                break
            except sqlite3.IntegrityError as e:
                # print("Integrity Error - Value Probably Already Exists")
                print("IntegrityError: {}".format(e))
                print(sql)
                break
            except sqlite3.OperationalError as e:
                print("Operation Error: {} - trying Again".format(e))
            except Exception as e:
                pass
                ex = "{}:{}".format(type(e).__name__, e)
                print(ex)