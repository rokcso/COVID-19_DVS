import query_database as qdatab
import datetime


# 获取数据更新时间
def get_data_update_time():
    sql = "select data_update_time from details_1 order by id desc limit 1"
    dataUpdateTime = qdatab.query_sql(sql)[0][0]
    gap = (datetime.datetime.now() - dataUpdateTime).seconds
    m_m, s = divmod(gap, 60)
    h, m = divmod(m_m, 60)
    res = 'Data updated in ' + str(dataUpdateTime)[0:-3] + ' (' + str(h) + 'h' + str(m) + 'm ago)'
    return res
