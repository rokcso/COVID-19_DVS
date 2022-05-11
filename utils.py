import pymysql
import datetime
#
#
# def mysql_conn():
#     """
#     连接 MySQL 数据库
#     :return: 返回游标, 连接
#     """
#     conn = pymysql.connect(host='124.221.238.251', user='root', password='@6769@mysql&hu', db='covid')
#     cursor = conn.cursor()
#     return cursor, conn
#
#
# def mysql_close(cursor, conn):
#     """
#     断开 MySQL 数据库连接
#     :return: None
#     """
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
#
#
# def mysql_query(sql, *args):
#     """
#     通用 MySQL 数据查询方法
#     :return: 查询结果
#     """
#     cursor = None
#     conn = None
#     cursor, conn = mysql_conn()
#     cursor.execute(sql, args)
#     res = cursor.fetchall()
#     mysql_close(cursor, conn)
#     return res
#
#
# def get_data_update_time():
#     """
#     查询 details 数据最近更新时间
#     :return: data_update_time
#     """
#     sql = "select data_update_time from details_1 order by id desc limit 1"
#     data_update_time = mysql_query(sql)[0][0]
#     gap = (datetime.datetime.now() - data_update_time).seconds
#     m_m, s = divmod(gap, 60)
#     h, m = divmod(m_m, 60)
#     res = 'Data updated in ' + str(data_update_time)[0:-3] + ' (' + str(h) + 'h' + str(m) + 'm ago)'
#     return res
#
#



def get_middle2_data():
    """
    :return: 各省数据
    """
    sql = "select prov_name, " \
          "sum(city_confirm_now) " \
          "from details_1 " \
          "where data_update_time = " \
              " (select data_update_time from details_1 order by data_update_time desc limit 1) " \
          "group by prov_name"
    res = mysql_query(sql)
    return res


def get_left1_data():
    """
    :return: 
    """
    sql1 = "select prov_name, " \
           "sum(city_confirm_now), " \
            "sum(city_confirm_add) " \
            "from details_1 " \
            "where data_update_time = " \
                "(select data_update_time from details_1 order by data_update_time  desc limit 1) " \
            "group by prov_name"
    # sql2 = "select prov_name from details_1 where data_update_time=(select data_update_time from details_1 order by data_update_time desc limit 1) group by prov_name"
    res1 = mysql_query(sql1)
    # res2 = mysql_query(sql2)
    return res1

if __name__ == "__main__":
    pass