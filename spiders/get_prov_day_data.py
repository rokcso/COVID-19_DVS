import traceback
import requests
import json
import time
import sys

sys.path.append("..")
import utils.query_database as qdatab


def crawl_prov_day_data():
    prov_list = ["台湾", "上海", "香港", "北京", "河南", "广东", "云南", "吉林", "辽宁", "贵州", "湖北", "陕西", "浙江", "福建", "黑龙江", "山东", "江苏",
                 "四川", "河北", "天津", "内蒙古", "广西", "湖南", "江西", "安徽", "新疆", "重庆", "甘肃", "山西", "海南", "宁夏", "青海", "澳门", "西藏"]

    url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="
    url_list = []
    for i in prov_list:
        url_list.append(url + i + "&limit=2")

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    res_list = []
    for i in url_list:
        res = requests.get(i, headers)
        res_text = json.loads(res.text)
        res_list.append(res_text["data"])

    prov_day_data = {}
    for i in res_list:
        prov_name = i[0]["province"]
        data_list = {}
        for j in i:
            date_time = str(j["year"]) + "." + str(j["date"])
            date_time_flag = time.strptime(date_time, "%Y.%m.%d")
            update_date = time.strftime("%Y-%m-%d", date_time_flag)

            # prov_name = j["province"]

            total_confirm = j["confirm"]
            total_dead = j["dead"]
            total_heal = j["heal"]
            now_confirm = int(total_confirm) - int(total_dead) - int(total_heal)
            add_confirm = j["newConfirm"]
            add_dead = j["newDead"]
            add_heal = j["newHeal"]

            # prov_day_data[update_date] = {"now_confirm": now_confirm,
            #                               "total_confirm": total_confirm,
            #                               "total_dead": total_dead,
            #                               "total_heal": total_heal,
            #                               "add_confirm": add_confirm,
            #                               "add_dead": add_dead,
            #                               "add_heal": add_heal
            #                               }
            data_list[update_date] = {"date": update_date,
                                      "now_confirm": now_confirm,
                                      "total_confirm": total_confirm,
                                      "total_dead": total_dead,
                                      "total_heal": total_heal,
                                      "add_confirm": add_confirm,
                                      "add_dead": add_dead,
                                      "add_heal": add_heal
                                      }
        prov_day_data[prov_name] = data_list
    return prov_day_data


def update_prov_day_data():
    conn = None
    cursor = None
    try:
        print(f"{time.asctime()} --> 开始获取 prov_day_data！")
        data = crawl_prov_day_data()
        print(f"{time.asctime()} --> 开始向 prov_day_list 更新数据！")
        conn, cursor = qdatab.connect_database()
        sql_1 = """
        
        insert into prov_day_list(
            update_date,
            prov_name,
            now_confirm,
            total_confirm,
            total_dead,
            total_heal,
            add_confirm,
            add_dead,
            add_heal) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        
        """
        sql_2 = "select total_confirm from prov_day_list where update_date = %s"

        for key_a, value_a in data.items():
            prov_name = key_a
            for key_b, value_b in value_a.items():
                # if not cursor.execute(sql_2, key_b):
                cursor.execute(sql_1, [key_b,
                                           prov_name,
                                           value_b.get("now_confirm"),
                                           value_b.get("total_confirm"),
                                           value_b.get("total_dead"),
                                           value_b.get("total_heal"),
                                           value_b.get("add_confirm"),
                                           value_b.get("add_dead"),
                                           value_b.get("add_heal")
                                           ])
        conn.commit()
        print(f"{time.asctime()} --> prov_day_list 表数据更新完毕！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)


if __name__ == "__main__":
    update_prov_day_data()  # 更新省份日更历史数据，注意：最好每天 00:01 更新