import traceback
import requests
import json
import time
import utils.query_database as qdatab


# 定义一个公用爬虫
def crawl_day_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    # url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    res = requests.get(url, headers)
    res_text = json.loads(res.text)
    res_data = json.loads(res_text["data"])
    return res_data


# 爬取中国每日数据
def crawl_china_day_list():
    res = crawl_day_data()

    china_day_list = {}
    for item in res["chinaDayList"]:
        date_time = item["y"] + "." + item["date"]
        date_time_flag = time.strptime(date_time, "%Y.%m.%d")
        last_update_time = time.strftime("%Y-%m-%d", date_time_flag)

        total_confirm = item["confirm"]  # 累计确诊
        total_dead = item["dead"]  # 累计死亡
        total_heal = item["heal"]  # 累计治愈
        total_imported_case = item["importedCase"]  # 累计境外输入
        total_no_infect = item["noInfect"]  # 累计无症状感染者
        now_confirm = item["nowConfirm"]  # 现有确诊
        now_local_confirm = item["localConfirm"]  # 现有本土确诊
        now_severe = item["nowSevere"]  # 现有重症
        dead_rate = item["deadRate"]  # 死亡率
        heal_rate = item["healRate"]  # 治愈率

        china_day_list[last_update_time] = {"total_confirm": total_confirm,
                                            "total_dead": total_dead,
                                            "total_heal": total_heal,
                                            "total_imported_case": total_imported_case,
                                            "total_no_infect": total_no_infect,
                                            "now_confirm": now_confirm,
                                            "now_local_confirm": now_local_confirm,
                                            "now_severe": now_severe,
                                            "dead_rate": dead_rate,
                                            "heal_rate": heal_rate
                                            }

    for item in res["chinaDayAddList"][1:]:
        date_time = item["y"] + "." + item["date"]
        date_time_flag = time.strptime(date_time, "%Y.%m.%d")
        last_update_time = time.strftime("%Y-%m-%d", date_time_flag)
        add_total_confirm = item["confirm"]  # 当日新增确诊
        add_total_dead = item["dead"]  # 当日新增死亡
        add_total_heal = item["heal"]  # 当日新增治愈
        add_total_imported_case = item["importedCase"]  # 当日新增境外输入
        add_total_no_infect = item["infect"]  # 当日新增无症状感染者
        add_total_local_no_infect = item["localinfectionadd"]  # 当日新增本地无症状感染者
        add_total_local_confirm = item["localConfirmadd"]  # 当日新增本地确诊

        china_day_list[last_update_time].update({"add_total_confirm": add_total_confirm,
                                                 "add_total_dead": add_total_dead,
                                                 "add_total_heal": add_total_heal,
                                                 "add_total_imported_case": add_total_imported_case,
                                                 "add_total_no_infect": add_total_no_infect,
                                                 "add_total_local_no_infect": add_total_local_no_infect,
                                                 "add_total_local_confirm": add_total_local_confirm
                                                 })

    return china_day_list


def update_china_day_list():
    conn = None
    cursor = None
    try:
        data = crawl_china_day_list()
        print(f"{time.asctime()} --> 开始向 china_day_list 表更新数据！")
        conn, cursor = qdatab.connect_database()
        sql_1 = "insert into china_day_list( " \
                "last_update_time, " \
                "total_confirm, " \
                "total_dead,  " \
                "total_heal, " \
                "total_imported_case, " \
                "total_no_infect, " \
                "now_confirm, " \
                "now_local_confirm, " \
                "now_severe, " \
                "dead_rate, " \
                "heal_rate, " \
                "add_total_confirm, " \
                "add_total_dead, " \
                "add_total_heal, " \
                "add_total_imported_case, " \
                "add_total_no_infect, " \
                "add_total_local_no_infect, " \
                "add_total_local_confirm) " \
                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql_2 = "select total_confirm from china_day_list where last_update_time = %s"
        for key, value in data.items():
            if not cursor.execute(sql_2, key):
                cursor.execute(sql_1, [key,
                                       value.get("total_confirm"),
                                       value.get("total_dead"),
                                       value.get("total_heal"),
                                       value.get("total_imported_case"),
                                       value.get("total_no_infect"),
                                       value.get("now_confirm"),
                                       value.get("now_local_confirm"),
                                       value.get("now_severe"),
                                       value.get("dead_rate"),
                                       value.get("heal_rate"),
                                       value.get("add_total_confirm"),
                                       value.get("add_total_dead"),
                                       value.get("add_total_heal"),
                                       value.get("add_total_imported_case"),
                                       value.get("add_total_no_infect"),
                                       value.get("add_total_local_no_infect"),
                                       value.get("add_total_local_confirm")
                                       ])
        conn.commit()
        print(f"{time.asctime()} --> china_day_list 表数据更新完毕！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)
