import requests
import json
import utils
import traceback
import time
import hashlib


def get_covid_data():
    """
    从腾讯获取当前最新数据：
    - 最新数据
    - 历史数据
    :return: history_covid_data, details_covid_data
    """

    # 获取数据的 API
    url_details = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=diseaseh5Shelf"
    url_history = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"

    # 执行请求的 headers 头
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    res_details = requests.get(url_details, headers)
    res_history = requests.get(url_history, headers)

    res_details_tag = json.loads(res_details.text)
    res_history_tag = json.loads(res_history.text)

    data_details = res_details_tag["data"]["diseaseh5Shelf"]
    data_history = res_history_tag["data"]

    history_covid_data = {}
    # print(f"{time.asctime()} --> 开始获取最新 history 数据")
    for item in data_history["chinaDayList"]:
        data_update_time_tag = item["y"] + "." + item["date"]
        now_time = time.strptime(data_update_time_tag, "%Y.%m.%d")
        # 修改数据更新时间的数据格式
        data_update_time = time.strftime("%Y-%m-%d", now_time)
        confirm = item["confirm"]  # 累计确诊人数
        confirm_now = item["nowConfirm"]  # 现存确诊人数
        suspect = item["suspect"]  # 疑似确诊人数
        heal = item["heal"]  # 累计治愈人数
        dead = item["dead"]  # 累计死亡人数
        history_covid_data[data_update_time] = {"confirm": confirm, "confirm_now": confirm_now, "suspect": suspect, "heal": heal, "dead": dead}

    for item in data_history["chinaDayAddList"][1:]:
        data_update_time_tag = item["y"] + "." + item["date"]
        now_time = time.strptime(data_update_time_tag, "%Y.%m.%d")
        # 修改数据更新时间的数据格式
        data_update_time = time.strftime("%Y-%m-%d", now_time)
        confirm_add = item["confirm"]
        suspect_add = item["suspect"]
        heal_add = item["heal"]
        dead_add = item["dead"]
        history_covid_data[data_update_time].update({"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})
    # print(f"{time.asctime()} --> 获取最新 history 数据完成")

    details_covid_data = []
    # print(f"{time.asctime()} --> 开始获取 details 数据")
    data_update_time = data_details["lastUpdateTime"]
    data_country = data_details["areaTree"]  # 全球各国家列表
    data_province = data_country[0]["children"]  # 中国各省列表
    for prov_info in data_province:
        prov_name = prov_info["name"]
        for city_info in prov_info["children"]:
            city_name = city_info["name"]
            city_confirm = city_info["total"]["confirm"]  # 累计确诊
            city_confirm_add = city_info["today"]["confirm"]  # 当日新增确诊
            city_confirm_now = city_info["total"]["nowConfirm"]  # 现存确诊
            city_heal = city_info["total"]["heal"]  # 累计治愈
            city_dead = city_info["total"]["dead"]  # 累计死亡
            details_covid_data.append([data_update_time, prov_name, city_name, city_confirm, city_confirm_add, city_confirm_now, city_heal, city_dead])
    # print(f"{time.asctime()} --> 获取 details 数据完成")
    return history_covid_data, details_covid_data


def get_risk_area_data():
    """
    获取国内中高风险地区数据
    :return:
    """
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
    res_1 = requests.post(url = url, data = json.dumps(post_param), headers = headers)
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


def up_details2mysql():
    """
    更新 details 中的数据到 MySQL 数据库
    :return: None
    """
    cursor = None
    conn = None
    try:
        li = get_covid_data()[1]
        print(f"{time.asctime()} --> 获取 details 数据")
        cursor, conn = utils.mysql_conn()
        sql = "insert into details_1(data_update_time, prov_name, city_name, city_confirm, city_confirm_add, city_confirm_now, city_heal, city_dead) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        sql_query = "select %s = (select data_update_time from details_1 order by id desc limit 1)"
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()} --> 开始更新 details 数据")
            for item in li:
                # cursor.execute(sql, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()} --> 更新 details 数据完成")
        else:
            print(f"{time.asctime()} --> details 已是最新数据！")
    except:
        traceback.print_exc()
    finally:
        utils.mysql_close(cursor, conn)


def up_history_data2mysql():
    """
    更新疫情历史数据到 MySQL
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = get_covid_data()[0]
        print(f"{time.asctime()} --> 获取 history 数据")
        cursor, conn = utils.mysql_conn()
        sql = "insert into history(data_update_time, confirm, confirm_add, confirm_now, suspect, suspect_add, heal, heal_add, dead, dead_add) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql_query = "select confirm from history where data_update_time = %s"
        for i, j in dic.items():
            if not cursor.execute(sql_query, i):
                print(f"{time.asctime()} --> 开始更新 history 数据")
                cursor.execute(sql, [i, j.get("confirm"), j.get("confirm_add"), j.get("confirm_now"), j.get("suspect"), j.get("suspect_add"), j.get("heal"), j.get("heal_add"), j.get("dead"), j.get("dead_add")])
                print(f"{time.asctime()} --> 更新 history 数据完成")
            else:
                print(f"{time.asctime()} --> history 已是最新数据！")
                break
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        utils.mysql_close(cursor, conn)


def up_risk_area_data2mysql():
    """
    更新中高风险地区数据到 MySQL 数据库
    :return:
    """
    cursor = None
    conn = None
    try:
        high_risk_area_list, middle_risk_area_list = get_risk_area_data()
        print(f"{time.asctime()} --> 获取 risk_area 数据")
        cursor, conn = utils.mysql_conn()
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
        utils.mysql_close(cursor, conn)


def main():
    """
    :return: 
    """
    up_details2mysql()
    up_history_data2mysql()
    up_risk_area_data2mysql()


if __name__ == '__main__':
    main()
