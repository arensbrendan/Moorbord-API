import pymysql

conn = pymysql.connect(host='69.247.163.204',
                               user="api",
                               password="o68aUqB6gegAyDd",
                               database='new',
                               cursorclass=pymysql.cursors.DictCursor)

sql = "SELECT * FROM user"
with conn.cursor() as db:
    db.execute(sql)
    results = db.fetchall()
    print(results)