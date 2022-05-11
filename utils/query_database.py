import pymysql


# 建立数据库连接
def connect_database():
    conn = pymysql.connect(host='124.221.238.251',
                           user='root',
                           password='@6769@mysql&hu',
                           db='covid',
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor


# 断开数据库连接
def close_database(cursor, conn):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


# 执行 SQL 语句
def query_sql(sql, *args):
    conn = None
    cursor = None
    conn, cursor = connect_database()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_database(cursor, conn)
    return res
