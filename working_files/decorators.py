import datetime
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()


def database_connect(func):
    def connect(ref, *args, **kwargs):
        conn = pymysql.connect(host='69.247.163.204',
                               user=os.getenv("DB_USER"),
                               password=os.getenv("DB_PASS"),
                               database='morboord',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as db:
                func_ret = func(ref, conn, *args, **kwargs)
        except Exception as error:
            raise
        else:
            conn.commit()
        finally:
            conn.close()
        return func_ret

    return connect


def block(func):
    def handler(*args, **kwargs):
        print("Hit catch block")
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)

    return handler


def hit(func):
    def handler(*args, **kwargs):
        print(f"Hit {func.__name__}")
        to_ret = func(*args, **kwargs)
        if to_ret is not None:
            return to_ret
    return handler

