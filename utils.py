# 自定义工具组件类

import time
import pymysql
from flask import jsonify

def get_local_time():
    """
    获取当前时间并拼装成字符串返回
    :return: 返回时间字符串
    """
    time_str = time.strftime('%Y {} %m {} %d {} %X')
    return time_str.format('年', '月', '日')

def mysql_conn():
    """
    连接 MySQL 数据库
    :return: 返回游标, 连接
    """
    conn = pymysql.connect(host='124.221.238.251', user='root', password='@6769@mysql&hu', db='covid')
    cursor = conn.cursor()
    return cursor, conn

def mysql_close(cursor, conn):
    """
    断开 MySQL 数据库连接
    :return: None
    """
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def mysql_query(sql, *args):
    """
    通用 MySQL 数据查询方法
    :return: 查询结果
    """
    cursor = None
    conn = None
    cursor, conn = mysql_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    mysql_close(cursor, conn)
    return res

def get_data_update_time():
    """
    查询 details 数据最近更新时间
    :return: data_update_time
    """
    sql = "select update_time from details order by id desc limit 1"
    data_update_time = mysql_query(sql)
    return str(data_update_time[0][0])

def get_middle_num():
    """
    查询基本数据用于数据大屏中间显示
    :return:
    """
    sql = "select sum(city_now_confirm), sum(city_today_confirm), sum(city_total_confirm), sum(city_total_heal), sum(city_total_dead) from details where update_time=(select update_time from details order by id desc limit 1)"
    res_1 = mysql_query(sql)[0]
    res = {"now_confirm": str(res_1[0]), "today_confirm": str(res_1[1]), "total_confirm": str(res_1[2]), "total_heal": str(res_1[3]), "total_dead": str(res_1[4])}
    return res

def get_middle2_data():
    """
    获取中间第二个视图，地图数据
    :return:
    """
    sql = "select distinct prov_name, prov_now_confirm from details where update_time = (select update_time from details order by update_time desc limit 1)"
    res_1 = mysql_query(sql)
    res = []
    for item in res_1:
        res.append({'name': item[0], 'value': item[1]})
    return {'data': res}

if __name__ == '__main__':
    print(get_middle2_data())