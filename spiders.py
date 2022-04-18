import requests
import json
import utils
import traceback
import time


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
    for item in data_history["chinaDayList"]:
        data_update_time_tag = item["y"] + "." + item["date"]
        now_time = time.strftime(data_update_time_tag, "%Y.%m.%d")
        # 修改数据更新时间的数据格式
        data_update_time = time.strftime("%Y-%m-%d", now_time)
        confirm = item["confirm"]  # 累计确诊人数
        confirm_now = item["confirm_now"]  # 现存确诊人数
        suspect = item["suspect"]  # 疑似确诊人数
        heal = item["heal"]  # 累计治愈人数
        dead = item["dead"]  # 累计死亡人数
        history_covid_data[data_update_time] = {"confirm": confirm, "confirm_now": confirm_now, "suspect": suspect,
                                                "heal": heal, "dead": dead}
    for item in data_history["chinaDayAddList"]:
        data_update_time_tag = item["y"] + "." + item["date"]
        now_time = time.strftime(data_update_time_tag, "%Y.%m.%d")
        # 修改数据更新时间的数据格式
        data_update_time = time.strftime("%Y-%m-%d", now_time)
        confirm_add = item["confirm"]
        suspect_add = item["suspect"]
        heal_add = item["heal"]
        dead_add = item["dead"]
        history_covid_data[data_update_time].update(
            {"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})

    details_covid_data = []
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
            details_covid_data.append(
                [data_update_time, prov_name, city_name, city_confirm, city_confirm_add, city_confirm_now, city_heal,
                 city_dead])
    return history_covid_data, details_covid_data


def up_details2mysql():
    """
    更新 details 中的数据到 MySQL 数据库
    :return: None
    """
    cursor = None
    conn = None
    try:
        details = get_covid_data()
        cursor, conn = utils.mysql_conn()
        # 更新数据的插入数据 MySQL 语句
        sql = "insert into details(update_time, prov_name, prov_now_confirm, prov_today_confirm, prov_total_confirm, prov_total_heal, prov_total_dead, city_name, city_now_confirm, city_today_confirm, city_total_confirm, city_total_heal, city_total_dead) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # sql_new_time 对比数据表中最新的数据更新时间与当前数据更新时间是否一致,若一致则没有新数据,则不更新
        sql_new_time = "select %s = (select update_time from details order by id desc limit 1)"
        cursor.execute(sql_new_time, details[0][0])
        # res = cursor.fetchall()
        if not cursor.fetchone()[0]:
            print(f'{time.asctime()} --> 开始更新 details 数据')
            for item in details:
                cursor.execute(sql, item)
            conn.commit()
            print(f'{time.asctime()} --> details 数据更新完毕')
        else:
            print(f'{time.asctime()} --> details 数据已是最新')
    except:
        traceback.print_exc()
    finally:
        utils.mysql_close(cursor, conn)


def main():
    get_covid_data()
    up_details2mysql()


if __name__ == '__main__':
    main()
