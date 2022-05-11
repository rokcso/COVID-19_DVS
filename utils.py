import pymysql
import datetime


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