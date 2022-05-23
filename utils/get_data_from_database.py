import json

import utils.query_database as qdatab
import datetime


# 获取数据更新时间
def get_data_update_time():
    sql = "select last_update_time from china_details order by id desc limit 1"
    dataUpdateTime = qdatab.query_sql(sql)[0][0]
    gap = (datetime.datetime.now() - dataUpdateTime).seconds
    m_m, s = divmod(gap, 60)
    h, m = divmod(m_m, 60)
    res = '数据更新于: ' + str(dataUpdateTime) + ' (' + str(h) + 'h' + str(m) + 'm' + str(s) + 's 前)'
    return res


def get_left2_data():
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select data_update_time, province, city, county, community, type " \
          "from risk_area " \
          "where data_update_time=(select data_update_time " \
          "from risk_area " \
          "order by data_update_time desc limit 1) "
    res = qdatab.query_sql(sql)
    return res


def get_num():
    """
    查询基本数据用于数据大屏中间显示
    :return:
    """
    sql = """
    
    select now_local_confirm,
          now_confirm,
          total_confirm,
          total_no_infect,
          total_imported_case,
          total_dead, 
          add_now_local_confirm,
          add_now_confirm,
          add_total_confirm,
          add_total_no_infect, 
          add_total_imported_case, 
          add_total_dead
          from china_details 
          where last_update_time = 
          (select last_update_time from china_details order by id desc limit 1)
    
    """
    res_1 = qdatab.query_sql(sql)[0]
    res = {"now_local_confirm": str(res_1[0]), "now_confirm": str(res_1[1]), "total_confirm": str(res_1[2]),
           "total_no_infect": str(res_1[3]), "total_imported_case": str(res_1[4]), "total_dead": str(res_1[5]),
           "add_now_local_confirm": str(res_1[6]), "add_now_confirm": str(res_1[7]), "add_total_confirm": str(res_1[8]),
           "add_total_no_infect": str(res_1[9]), "add_total_imported_case": str(res_1[10]),
           "add_total_dead": str(res_1[11])}
    if int(res_1[6]) > 0:
        res_a1 = "+" + str(res_1[6])
        res.update({"add_now_local_confirm": res_a1})
    elif int(res_1[6]) < 0:
        res_a1 = "-" + str(res_1[6])
        res.update({"add_now_local_confirm": res_a1})
    else:
        pass

    if int(res_1[7]) > 0:
        res_a1 = "+" + str(res_1[7])
        res.update({"add_now_confirm": res_a1})
    elif int(res_1[7]) < 0:
        res_a1 = "-" + str(res_1[7])
        res.update({"add_now_confirm": res_a1})
    else:
        pass

    if int(res_1[8]) > 0:
        res_a1 = "+" + str(res_1[8])
        res.update({"add_total_confirm": res_a1})
    elif int(res_1[8]) < 0:
        res_a1 = "-" + str(res_1[8])
        res.update({"add_total_confirm": res_a1})
    else:
        pass

    if int(res_1[9]) > 0:
        res_a1 = "+" + str(res_1[9])
        res.update({"add_total_no_infect": res_a1})
    elif int(res_1[9]) < 0:
        res_a1 = "-" + str(res_1[9])
        res.update({"add_total_no_infect": res_a1})
    else:
        pass

    if int(res_1[10]) > 0:
        res_a1 = "+" + str(res_1[10])
        res.update({"add_total_imported_case": res_a1})
    elif int(res_1[10]) < 0:
        res_a1 = "-" + str(res_1[10])
        res.update({"add_total_imported_case": res_a1})
    else:
        pass

    if int(res_1[11]) > 0:
        res_a1 = "+" + str(res_1[11])
        res.update({"add_total_dead": res_a1})
    elif int(res_1[11]) < 0:
        res_a1 = "-" + str(res_1[11])
        res.update({"add_total_dead": res_a1})
    else:
        pass

    return res


# 获取 index00 页面地图数据
def get_middle_data():
    sql = """
    
    select prov_name, prov_now_confirm, prov_add_now_confirm, prov_total_confirm
from prov_details
where last_update_time = 
(select last_update_time from prov_details order by id desc limit 1)
    
    """
    res = qdatab.query_sql(sql)
    return res


# 获取 left-1 数据
def get_left1_data():
    sql = """
    
    SELECT update_date, prov_name, now_confirm, add_confirm, total_confirm
    FROM prov_day_list
    WHERE substr(update_date, 1, 10) between substr(date_sub(now(), INTERVAL 15 DAY), 1, 10) and substr(date_sub(now(), interval 1 day), 1, 10)
    """

    res = qdatab.query_sql(sql)
    return res


def get_left1_first_data():
    sql = """
    
     SELECT update_date, sum(now_confirm), sum(add_confirm), sum(total_confirm)
    FROM prov_day_list
    WHERE substr(update_date, 1, 10) between substr(date_sub(now(), INTERVAL 14 DAY), 1, 10) and now()
    group by update_date
    
    """
    res = qdatab.query_sql(sql)
    return res


# 获取 right-1 数据
def get_right1_data():
    sql = """

    SELECT prov_name, city_name, city_now_confirm, city_add_now_confirm, city_total_confirm FROM `city_details`
    WHERE last_update_time = (SELECT last_update_time FROM city_details ORDER BY id DESC LIMIT 1)

    """

    res = qdatab.query_sql(sql)
    return res


def get_bottom_data():
    # 找出新增确诊人数最多的 TOP 省份
    sql2 = """

        select prov_name, sum(add_confirm)
        from prov_day_list
        WHERE substr(update_date, 1, 10) between substr(date_sub(now(), INTERVAL 60 DAY), 1, 10) and now()
        group by prov_name
        order by sum(add_confirm) desc

    """
    res2 = qdatab.query_sql(sql2)
    prov_list = []
    for i in range(0, 7):
        prov_list.append(res2[i][0])
    prov_list = prov_list[::-1]

    # 根据上方省份查询数据
    sql = """
    
    SELECT update_date, prov_name, now_confirm, add_confirm, total_confirm
    FROM prov_day_list
    WHERE substr(update_date, 1, 10) 
    between substr(date_sub(now(), INTERVAL 61 DAY), 1, 10) 
    and substr(date_sub(now(), interval 2 day), 1, 10)
    and prov_name in %s
    order by case when prov_name = %s then 1
    when prov_name = %s then 2
    when prov_name = %s then 3
    when prov_name = %s then 4
    when prov_name = %s then 5
    when prov_name = %s then 6
    when prov_name = %s then 7
    end
    
    """
    res = qdatab.query_sql(sql, prov_list, prov_list[0], prov_list[1], prov_list[2], prov_list[3], prov_list[4],
                           prov_list[5], prov_list[6])

    # 获取日期列表
    date1 = []
    for i in range(2, 62):
        temp_date = datetime.datetime.now()
        aa = (temp_date + datetime.timedelta(days=-i)).strftime("%m.%d")
        date1.append(aa)
    date = date1[::-1]

    # 构建 data 数据的坐标部分数据
    add_data = []
    for i in range(0, len(prov_list)):
        for j in range(0, len(date)):
            f = [i, j]
            add_data.append(f)

    for i in range(0, len(prov_list)):
        for j in range(0, len(res)):
            if res[j][1] == prov_list[i]:
                add_data[j].append(res[j][3])

    return prov_list, date, add_data
