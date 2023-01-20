import datetime
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()


def database_connect(func):
    def connect(*args, **kwargs):
        conn = pymysql.connect(host='69.247.163.204',
                               user=os.getenv("DB_USER"),
                               password=os.getenv("DB_PASS"),
                               database='morboord',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            func_ret = func(conn, *args, **kwargs)
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
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)

    return handler


@database_connect
def log(conn, file):
    def upper(func):
        def handler(*args, **kwargs):
            print(f"Hit {func.__name__} from file {file}")
            to_ret = func(*args, **kwargs)
            try:
                with conn.cursor() as db:
                    sql = "INSERT INTO log(log, user_id) VALUES ('%s', 1)" % str(func.__name__)
                    db.execute(sql)
                    conn.commit()
            except Exception as error:
                print(str(error))

            if to_ret is not None:
                return to_ret
        return handler

    return upper
