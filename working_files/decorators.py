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
                               database='new',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as db:
                func_ret = func(ref, db, *args, **kwargs)
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


def log(file):
    def upper(func):
        def handler(*args, **kwargs):
            conn = pymysql.connect(host='69.247.163.204',
                                   user=os.getenv("DB_USER"),
                                   password=os.getenv("DB_PASS"),
                                   database='new',
                                   cursorclass=pymysql.cursors.DictCursor)
            u_name = args[2].username
            print(f"Hit {func.__name__} from file {file}")
            to_ret = func(*args, **kwargs)
            try:
                with conn.cursor() as db:
                    sql = "SELECT user_id FROM user WHERE username = '%s'" % u_name
                    db.execute(sql)
                    results = db.fetchone()
                    sql = "INSERT INTO log(log, user_id) VALUES ('%s', %s)" % (str(func.__name__), results['user_id'])
                    db.execute(sql)
                    conn.commit()
            except Exception as error:
                print(str(error))

            if to_ret is not None:
                return to_ret
        return handler

    return upper
