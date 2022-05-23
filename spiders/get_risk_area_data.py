import traceback
import requests
import time
import hashlib
import json
import sys

sys.path.append("..")
import utils.query_database as qdatab


def crawl_risk_area_data():
    # 时间戳
    a = "%.3f" % (time.time() / 1e3)
    b = a.replace(".", "")
    c = "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA"
    d = "123456789abcdefg"

    sig_1 = hashlib.sha256()
    sig_1.update(str(b + c + d + b).encode("utf8"))
    sig_1 = sig_1.hexdigest().upper()

    sig_2 = hashlib.sha256()
    sig_2.update(str(b + "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA" + b).encode("utf8"))
    sig_2 = sig_2.hexdigest().upper()

    post_param = {
        "appId": "NcApplication",
        "key": "3C502C97ABDA40D0A60FBEE50FAAD1DA",
        "nonceHeader": "123456789abcdefg",
        "paasHeader": "zdww",
        "signatureHeader": sig_1,
        "timestampHeader": b
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "http://bmfw.www.gov.cn/",
        "Origin": "http://bmfw.www.gov.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "x-wif-nonce": "QkjjtiLM2dCratiA",
        "x-wif-paasid": "smt-application",
        "x-wif-signature": sig_2,
        "x-wif-timestamp": b,
    }

    url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"
    res_1 = requests.post(url=url, data=json.dumps(post_param), headers=headers)
    res_2 = res_1.text
    res = json.loads(res_2)

    data_update_time = res["data"]["end_update_time"]
    high_risk_area_cnt = res["data"].get("hcount", 0)
    middle_risk_area_cnt = res["data"].get("mcount", 0)

    high_risk_area_list_1 = res["data"]["highlist"]
    middle_risk_area_list_1 = res["data"]["middlelist"]

    high_risk_area_list = []
    middle_risk_area_list = []
    # print(f"{time.asctime()} --> 开始获取 risk_area 数据")
    for item in high_risk_area_list_1:
        type = "高风险"
        province = item["province"]
        city = item["city"]
        county = item["county"]
        area_name = item["area_name"]
        communitys = item["communitys"]
        for item in communitys:
            high_risk_area_list.append([data_update_time, province, city, county, item, type])

    for item in middle_risk_area_list_1:
        type = "中风险"
        province = item["province"]
        city = item["city"]
        county = item["county"]
        area_name = item["area_name"]
        communitys = item["communitys"]
        for item in communitys:
            middle_risk_area_list.append([data_update_time, province, city, county, item, type])
    # print(f"{time.asctime()} --> 获取 risk_area 数据完成")
    return high_risk_area_list, middle_risk_area_list


def update_risk_area_data():
    conn = None
    cursor = None
    try:
        high_risk_area_list, middle_risk_area_list = crawl_risk_area_data()
        print(f"{time.asctime()} --> 获取 risk_area 数据")
        conn, cursor = qdatab.connect_database()
        sql = "insert into risk_area(data_update_time, province, city, county, community, type) values(%s, %s, %s, %s, %s, %s)"
        sql_query = "select %s = (select data_update_time from risk_area order by id desc limit 1)"
        cursor.execute(sql_query, high_risk_area_list[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()} --> 开始更新 risk_area 数据")
            for item in high_risk_area_list:
                cursor.execute(sql, item)
            for item in middle_risk_area_list:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()} --> 更新 risk_area 数据完成")
        else:
            print(f"{time.asctime()} --> risk_area 已是最新数据！")
    except:
        traceback.print_exc()
    finally:
        qdatab.close_database(conn, cursor)


if __name__ == "__main__":
    update_risk_area_data()
