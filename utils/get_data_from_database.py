import utils.query_database as qdatab
import datetime


# 获取数据更新时间
def get_data_update_time():
    sql = "select last_update_time from china_details order by id desc limit 1"
    dataUpdateTime = qdatab.query_sql(sql)[0][0]
    gap = (datetime.datetime.now() - dataUpdateTime).seconds
    m_m, s = divmod(gap, 60)
    h, m = divmod(m_m, 60)
    res = 'Data updated in ' + str(dataUpdateTime)[0:-3] + ' (' + str(h) + 'h' + str(m) + 'm ago)'
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
           "add_total_no_infect": str(res_1[9]), "add_total_imported_case": str(res_1[10]), "add_total_dead": str(res_1[11])}
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
