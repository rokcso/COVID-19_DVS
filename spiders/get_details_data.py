import time
import traceback
import requests
import json
import utils.query_database as qdatab


# 定义一个公用爬虫
def crawl_tencent_h5():
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=diseaseh5Shelf"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    res = requests.get(url, headers)
    res_text = json.loads(res.text)
    res_data = res_text["data"]["diseaseh5Shelf"]
    return res_data


# 爬取全国累计数据和中国每日新增数据
def crawl_china_details():
    res = crawl_tencent_h5()

    # 存储中国累计数据和中国每日新增数据表
    china_details = {}

    # 解析数据
    last_update_time = res["lastUpdateTime"]  # 最近更新时间
    # chinaTotal ==> 累计数据
    total_confirm = res["chinaTotal"]["confirm"]  # 累计确诊
    total_dead = res["chinaTotal"]["dead"]  # 累计死亡
    total_heal = res["chinaTotal"]["heal"]  # 累计治愈
    total_imported_case = res["chinaTotal"]["importedCase"]  # 累计境外输入
    total_no_infect = res["chinaTotal"]["noInfect"]  # 累计无症状感染者
    # chinaNow ==> 现有数据
    now_confirm = res["chinaTotal"]["nowConfirm"]  # 现有确诊
    now_local_confirm = res["chinaTotal"]["localConfirmH5"]  # 现有本土确诊
    now_severe = res["chinaTotal"]["nowSevere"]  # 现有重症
    # chinaAdd ==> 当日新增数据
    add_total_confirm = res["chinaAdd"]["confirm"]  # 累计确诊当日变化数据
    add_total_dead = res["chinaAdd"]["dead"]  # 累计死亡当日变化数据
    add_total_heal = res["chinaAdd"]["heal"]  # 累计治愈当日变化数据
    add_total_imported_case = res["chinaAdd"]["importedCase"]  # 累计境外输入当日变化数据
    add_total_no_infect = res["chinaAdd"]["noInfect"]  # 累计无症状感染者当日变化数据
    add_now_confirm = res["chinaAdd"]["nowConfirm"]  # 现有确诊当日变化数据
    add_now_local_confirm = res["chinaAdd"]["localConfirmH5"]  # 现有本土确诊当日变化数据
    add_now_severe = res["chinaAdd"]["nowSevere"]  # 现有重症当日变化数据

    # 将数据存字典
    china_details[last_update_time] = {"totalConfirm": total_confirm,
                                       "totalDead": total_dead,
                                       "totalHeal": total_heal,
                                       "totalImportedCase": total_imported_case,
                                       "totalNoInfect": total_no_infect,
                                       "nowConfirm": now_confirm,
                                       "nowLocalConfirm": now_local_confirm,
                                       "nowSevere": now_severe,
                                       "addTotalConfirm": add_total_confirm,
                                       "addTotalDead": add_total_dead,
                                       "addTotalHeal": add_total_heal,
                                       "addTotalImportedCase": add_total_imported_case,
                                       "addTotalNoInfect": add_total_no_infect,
                                       "addNowConfirm": add_now_confirm,
                                       "addNowLocalConfirm": add_now_local_confirm,
                                       "addNowSevere": add_now_severe
                                       }

    return china_details


# 爬取省级数据
def crawl_prov_details():
    res = crawl_tencent_h5()

    # 存储省级数据
    prov_details = []
    # 解析数据
    last_update_time = res["lastUpdateTime"]
    # 进一步定位省级别数据
    prov_data = res["areaTree"][0]["children"]
    for item in prov_data:
        prov_name = item["name"]  # 省份名称
        if len(item["adcode"]) >= 1:
            prov_adcode = item["adcode"]  # 地区编码
        else:
            prov_adcode = '0'
        # total ==> 累计数据
        prov_total_confirm = item["total"]["confirm"]  # 累计确诊
        prov_total_dead = item["total"]["dead"]  # 累计死亡
        prov_total_heal = item["total"]["heal"]  # 累计治愈
        # now ==> 现有数据
        prov_now_confirm = item["total"]["nowConfirm"]  # 现有确诊
        prov_now_no_infect = item["total"]["wzz"]  # 现有无症状感染者
        # add ==> 当日新增数据
        prov_add_now_confirm = item["today"]["confirm"]  # 现有确诊当日变化数据
        prov_add_now_local_confirm = item["today"]["local_confirm_add"]  # 现有本土确诊当日变化数据
        prov_add_now_no_infect = item["today"]["wzz_add"]  # 现有无症状感染者当日变化数据
        prov_details.append([last_update_time,
                             prov_name,
                             prov_adcode,
                             prov_total_confirm,
                             prov_total_dead,
                             prov_total_heal,
                             prov_now_confirm,
                             prov_now_no_infect,
                             prov_add_now_confirm,
                             prov_add_now_local_confirm,
                             prov_add_now_no_infect
                             ])

    return prov_details


# 爬取市级数据
def crawl_city_details():
    res = crawl_tencent_h5()

    # 存储市级数据
    city_details = []
    last_update_time = res["lastUpdateTime"]
    prov_data = res["areaTree"][0]["children"]
    for i in prov_data:
        prov_name = i["name"]
        for j in i["children"]:
            city_name = j["name"]
            if len(j["adcode"]) >= 1:
                city_adcode = j["adcode"]  # 地区代码
            else:
                city_adcode = '0'
            # total ==> 累计数据
            city_total_confirm = j["total"]["confirm"]  # 累计确诊
            city_total_dead = j["total"]["dead"]  # 累计死亡
            city_total_heal = j["total"]["heal"]  # 累计治愈
            # now ==> 现有数据
            city_now_confirm = j["total"]["nowConfirm"]  # 现有确诊
            city_now_no_infect = j["total"]["wzz"]  # 现有无症状感染者
            # add ==> 当日新增数据
            city_add_now_confirm = j["today"]["confirm"]  # 现有确诊当日变化数据
            if len(j["today"]["wzz_add"]) >= 1:
                city_add_now_no_infect = j["today"]["wzz_add"]  # 现有无症状感染者当日变化数据
            else:
                city_add_now_no_infect = '0'
            city_details.append([last_update_time,
                                 prov_name,
                                 city_name,
                                 city_adcode,
                                 city_total_confirm,
                                 city_total_dead,
                                 city_total_heal,
                                 city_now_confirm,
                                 city_now_no_infect,
                                 city_add_now_confirm,
                                 city_add_now_no_infect
                                 ])

    return city_details


# 将 china_details 插入数据库
def update_china_details():
    conn = None
    cursor = None
    try:
        data = crawl_china_details()
        print(f"{time.asctime()} --> 开始向 china_details 表更新数据！")
        conn, cursor = qdatab.connect_database()
        sql_1 = "insert into china_details( " \
                "last_update_time, " \
                "total_confirm, " \
                "total_dead, " \
                "total_heal, " \
                "total_imported_case, " \
                "total_no_infect, " \
                "now_confirm, " \
                "now_local_confirm, " \
                "now_severe, " \
                "add_total_confirm, " \
                "add_total_dead, " \
                "add_total_heal, " \
                "add_total_imported_case, " \
                "add_total_no_infect, " \
                "add_now_confirm, " \
                "add_now_local_confirm, " \
                "add_now_severe) " \
                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql_2 = "select total_confirm from china_details where last_update_time = %s"
        for key, value in data.items():
            if not cursor.execute(sql_2, key):
                cursor.execute(sql_1, [key,
                                       value.get("totalConfirm"),
                                       value.get("totalDead"),
                                       value.get("totalHeal"),
                                       value.get("totalImportedCase"),
                                       value.get("totalNoInfect"),
                                       value.get("nowConfirm"),
                                       value.get("nowLocalConfirm"),
                                       value.get("nowSevere"),
                                       value.get("addTotalConfirm"),
                                       value.get("addTotalDead"),
                                       value.get("addTotalHeal"),
                                       value.get("addTotalImportedCase"),
                                       value.get("addTotalNoInfect"),
                                       value.get("addNowConfirm"),
                                       value.get("addNowLocalConfirm"),
                                       value.get("addNowSevere")
                                       ])
        conn.commit()
        print(f"{time.asctime()} --> china_details 表数据更新完毕！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)


# 更新 prov_details 数据
def update_prov_details():
    conn = None
    cursor = None
    try:
        data = crawl_prov_details()
        conn, cursor = qdatab.connect_database()
        sql1 = "insert into prov_details( " \
               "last_update_time, " \
               "prov_name, " \
               "prov_adcode, " \
               "prov_total_confirm, " \
               "prov_total_dead, " \
               "prov_total_heal, " \
               "prov_now_confirm, " \
               "prov_now_no_infect, " \
               "prov_add_now_confirm, " \
               "prov_add_now_local_confirm, " \
               "prov_add_now_no_infect) " \
               "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql2 = "select %s = (select last_update_time from prov_details order by id desc limit 1)"
        cursor.execute(sql2, data[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()} --> 开始向 prov_details 表更新数据！")
            for item in data:
                cursor.execute(sql1, item)
            conn.commit()
            print(f"{time.asctime()} --> prov_details 表数据更新完毕！")
        else:
            print(f"{time.asctime()} --> prov_details 表数据已是最新！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)


# 更新 city_details 数据
def update_city_details():
    conn = None
    cursor = None
    try:
        data = crawl_city_details()
        conn, cursor = qdatab.connect_database()
        sql1 = "insert into city_details( " \
               "last_update_time, " \
               "prov_name, " \
               "city_name, " \
               "city_adcode, " \
               "city_total_confirm, " \
               "city_total_dead, " \
               "city_total_heal, " \
               "city_now_confirm, " \
               "city_now_no_infect, " \
               "city_add_now_confirm, " \
               "city_add_now_no_infect) " \
               "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql2 = "select %s = (select last_update_time from city_details order by id desc limit 1)"
        cursor.execute(sql2, data[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()} --> 开始向 city_details 表更新数据！")
            for item in data:
                cursor.execute(sql1, item)
            conn.commit()
            print(f"{time.asctime()} --> city_details 表数据更新完毕！")
        else:
            print(f"{time.asctime()} --> city_details 表数据已是最新！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)


if __name__ == "__main__":
    update_china_details()
    update_prov_details()
    update_city_details()
