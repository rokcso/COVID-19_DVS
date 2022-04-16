import requests
import json
import utils
import traceback
import time

def get_now_data():
    """
    从腾讯获取当前最新数据
    :return: details 具体到省市区的详细数据
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    res = requests.get(url, headers)
    res_json = json.loads(res.text)
    res_data = json.loads(res_json["data"]) # 总目标数据
    res_china = res_data["areaTree"][0] # 中国省市详细数据

    # 存储当前最新详细数据，具体到省市区
    details = []
    details_prov = []
    details_city = []
    update_time = res_data["lastUpdateTime"]
    for prov_i in res_china["children"]:
        prov_name = prov_i["name"]
        prov_now_confirm = prov_i["total"]["nowConfirm"] # 省级当前现存确诊
        prov_total_confirm = prov_i["total"]["confirm"] # 省级累计确诊
        prov_total_dead = prov_i["total"]["dead"] # 省级累计死亡
        prov_total_heal = prov_i["total"]["heal"] # 省级累计治愈
        prov_today_confirm = prov_i["today"]["confirm"] # 省级今日新增确诊
        # details_prov.append(
        #     [update_time, prov_name, prov_now_confirm, prov_today_confirm, prov_total_confirm,
        #      prov_total_heal, prov_total_dead])
        for city_i in prov_i["children"]:
            city_name = city_i["name"]
            city_now_confirm = city_i["total"]["nowConfirm"]  # 市级当前现存确诊
            city_total_confirm = city_i["total"]["confirm"] # 市级累计确诊
            city_total_dead = city_i["total"]["dead"] # 市级累计死亡
            city_total_heal = city_i["total"]["heal"] # 市级累计治愈
            city_today_confirm = city_i["today"]["confirm"] # 市级今日新增确诊
            # details_city.append([update_time, city_name, city_now_confirm, city_today_confirm,
            #                      city_total_confirm, city_total_heal, city_total_dead])
            details.append([update_time, prov_name, prov_now_confirm, prov_today_confirm, prov_total_confirm, prov_total_heal, prov_total_dead, city_name, city_now_confirm, city_today_confirm, city_total_confirm, city_total_heal, city_total_dead])
    # return details_prov, details_city
    return details

def up_details2mysql():
    """
    更新 details 中的数据到 MySQL 数据库
    :return: None
    """
    cursor = None
    conn = None
    try:
        details = get_now_data()
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
    get_now_data()
    up_details2mysql()

if __name__ == '__main__':
    main()