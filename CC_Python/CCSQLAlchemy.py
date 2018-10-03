import sqlite3
from venv import logger

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.exc import IntegrityError, OperationalError


class CCSQLAlchemy:
    def __init__(self, database=""):
        if database != "":
            self.database = database
            self.engine = create_engine(self.database)
            self.conn = ""

    def connect(self):
        self.conn = self.engine.connect()

    def gettablenames(self):
        return self.engine.table_names()

    def gettable(self, tname):
        metadata = MetaData()
        table = Table(tname, metadata, autoload=True, autoload_with=self.engine)
        return table

    def executesql(self, sql):
        results_proxy = self.conn.execute(sql)
        results = results_proxy.fetchall()
        return results

    def runsql(self, conn, sql):
        cursor = conn.cursor()
        while True:
            try:
                cursor.execute(sql)
                conn.commit()
                break
            except IntegrityError as e:
                # print("Integrity Error - Value Probably Already Exists")
                logger.error("IntegrityError: {}".format(e))
                logger.error(sql)
                break
            except OperationalError as e:
                logger.error("Operation Error: {} - trying Again".format(e))
            except Exception as e:
                pass
                ex = "{}:{}".format(type(e).__name__, e)
                logger.error(ex)


    def select(self, tname):
        table = self.gettable(tname)

    def insert(self, table, cols):
        metadata = MetaData()
        conn = self.engine.connect()
        table = Table(table, metadata, autoload=True, autoload_with=self.engine)
        while True:
            try:
                ins = table.insert().values(cols)
                conn.execute(ins)
                break
            except IntegrityError as e:
                # print("Integrity Error - Value Probably Already Exists")
                logger.error("IntegrityError: {}".format(e))
                break
            except OperationalError as e:
                logger.error("Operation Error: {} - trying Again".format(e))
            except Exception as e:
                if type(e).__name__ == "IntegrityError":
                    break
                elif type(e).__name__ == "IntegrityError":
                    logger.error("Operation Error: {} - trying Again".format(e))
                    pass
                else:
                    ex = "{}:{}".format(type(e).__name__, e)
                    logger.error(ex)
                    pass
