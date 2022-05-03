import pymysql
import datetime


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
    sql = "select data_update_time from details_1 order by id desc limit 1"
    data_update_time = mysql_query(sql)[0][0]
    gap = (datetime.datetime.now() - data_update_time).seconds
    m_m, s = divmod(gap, 60)
    h, m = divmod(m_m, 60)
    res = 'Data updated in ' + str(data_update_time)[0:-3] + ' (' + str(h) + 'h' + str(m) + 'm ago)'
    return res


def get_middle1_num():
    """
    查询基本数据用于数据大屏中间显示
    :return:
    """
    sql = "select confirm_now, confirm_add, suspect, suspect_add, heal, heal_add, dead, dead_add from history where data_update_time  = (select data_update_time from history order by id desc limit 1)"
    res_1 = mysql_query(sql)[0]
    res = {"confirm_now": str(res_1[0]), "confirm_add": str(res_1[1]), "suspect": str(res_1[2]), "suspect_add": str(res_1[3]), "heal": str(res_1[4]), "heal_add": str(res_1[5]), "dead": str(res_1[6]), "dead_add": str(res_1[7])}
    if res_1[1] > 0:
        res_a1 = "+" + str(res_1[1])
        res.update({"confirm_add": res_a1})
    elif int(res_1[1]) < 0:
        res_a1 = "-" + str(res_1[1])
        res.update({"confirm_add": res_a1})
    else:
        pass
    if res_1[3] > 0:
        res_a3 = "+" + str(res_1[3])
        res.update({"suspect_add": res_a3})
    elif int(res_1[3]) < 0:
        res_a3 = "-" + str(res_1[3])
        res.update({"suspect_add": res_a3})
    else:
        pass
    if res_1[5] > 0:
        res_a5 = "+" + str(res_1[5])
        res.update({"heal_add": res_a5})
    elif int(res_1[5]) < 0:
        res_a5 = "-" + str(res_1[5])
        res.update({"heal_add": res_a5})
    else:
        pass
    if res_1[7] > 0:
        res_a7 = "+" + str(res_1[7])
        res.update({"dead_add": res_a7})
    elif int(res_1[7]) < 0:
        res_a7 = "-" + str(res_1[7])
        res.update({"dead_add": res_a7})
    else:
        pass
    return res


def get_middle2_data():
    """
    获取中间第二个视图，地图数据
    :return:
    """
    sql = "select prov_name, sum(city_confirm_now) from details_1 where data_update_time = (select data_update_time from details_1 order by id desc limit 1) group by prov_name"
    res_1 = mysql_query(sql)
    res = []
    for item in res_1:
        res.append({"name": item[0], "value": int(item[1])})
    return {"data": res}


if __name__ == '__main__':
    pass