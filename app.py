# -*- coding: UTF-8 -*-


import datetime
from flask import Flask, jsonify
from flask import render_template
import utils.get_data_from_database as gdfdb

# 初始化一个 Python Flask App 对象
app = Flask(__name__)


# 创建一个路由，路径在根目录「/」下，允许的请求方式有 GET、POST
@app.route('/', methods=['GET', 'POST'])
def root():
    """
    返回一个 HTML 模板文件
    :return: 
    """
    return render_template('index.html')


@app.route('/index00', methods=['GET', 'POST'])
def index00():
    """
    返回一个 HTML 模板文件
    :return:
    """
    return render_template('index00.html')


# @app.route('/index01', methods=['GET', 'POST'])
# def index01():
#     """
#     返回一个 HTML 模板文件
#     :return:
#     """
#     return render_template('index01.html')


@app.errorhandler(404)
def not_found(error):
    """
    请求返回 404 时返回一个 404 页面
    :param error:
    :return:
    """
    return render_template('404.html', result=404)


# 创建获取数据更新时间的路由
@app.route('/get_data_update_time', methods=['GET', 'POST'])
def get_data_update_time():
    """
    返回数据更新时间：
    - 'Data updated in 2022-04-18 12:34 (2h42m ago)'
    :return: data_update_time
    """
    return gdfdb.get_data_update_time()


# 创建获取 middle1 位置的数字数据的路由
@app.route('/get_num', methods=['GET', 'POST'])
def get_num():
    """
    返回 middle1 位置的数字数据：
    :return:
    """
    return gdfdb.get_num()


# 创建获取 middle 位置的地图数据
@app.route('/get_middle_data', methods=['GET', 'POST'])
def get_middle_data():
    res_1 = gdfdb.get_middle_data()
    res = {"now_confirm": ([{"name": res_1[0][0], "value": res_1[0][1]}]),
           "add_now_confirm": ([{"name": res_1[0][0], "value": res_1[0][2]}]),
           "total_confirm": ([{"name": res_1[0][0], "value": res_1[0][3]}])}
    for i in range(1, len(res_1)):
        res["now_confirm"].append({"name": res_1[i][0], "value": res_1[i][1]})
    for i in range(1, len(res_1)):
        res["add_now_confirm"].append({"name": res_1[i][0], "value": res_1[i][2]})
    for i in range(1, len(res_1)):
        res["total_confirm"].append({"name": res_1[i][0], "value": res_1[i][3]})
    return jsonify(res)


@app.route('/get_left1_data', methods=['GET', 'POST'])
def get_left1_data():
    res = gdfdb.get_left1_data()
    # day_data = []
    # data = {}
    # for i in res:
    #     for j in res:
    #         day_data.append({"date": str(j[0])[5:10], "now_confirm": j[2], "add_now_confirm": j[3], "total_confirm": j[4]})
    #     data[i[1]] = day_data
    # res_data = jsonify(data)

    prov_list = ["台湾", "上海", "香港", "北京", "河南", "广东", "云南", "吉林", "辽宁", "贵州", "湖北", "陕西", "浙江", "福建", "黑龙江", "山东", "江苏",
                 "四川", "河北", "天津", "内蒙古", "广西", "湖南", "江西", "安徽", "新疆", "重庆", "甘肃", "山西", "海南", "宁夏", "青海", "澳门", "西藏"]
    date, now_confirm, add_now_confirm, total_confirm = [], [], [], []
    now_confirm1, add_now_confirm1, total_confirm1 = [], [], []
    for j in prov_list:
        now_confirm, add_now_confirm, total_confirm = [], [], []
        for i in res:
            # date.append(str(i[0])[5:10])
            if j == i[1]:
                now_confirm.append(int(i[2]))
                add_now_confirm.append(int(i[3]))
                total_confirm.append(int(i[4]))
        now_confirm1.append(now_confirm)
        add_now_confirm1.append(add_now_confirm)
        total_confirm1.append(total_confirm)

    for i in range(1, 15):
        temp_date = datetime.datetime.now()
        aa = (temp_date + datetime.timedelta(days=-i)).strftime("%m.%d")
        date.append(aa)

    return jsonify(
        {"date": date[::-1], "prov_name": prov_list, "now_confirm": now_confirm1, "add_now_confirm": add_now_confirm1,
         "total_confirm": total_confirm1})


@app.route('/get_left1_first_data', methods=['GET', 'POST'])
def get_left1_first_data():
    res = gdfdb.get_left1_first_data()
    date, now_confirm1, add_now_confirm1, total_confirm1 = [], [], [], []
    for i in res:
        now_confirm1.append(int(i[1]))
        add_now_confirm1.append(int(i[2]))
        total_confirm1.append(int(i[3]))
    for i in range(0, 14):
        temp_date = datetime.datetime.now()
        aa = (temp_date + datetime.timedelta(days=-i)).strftime("%m.%d")
        date.append(aa)
    return jsonify({"date": date[::-1], "now_confirm": now_confirm1, "add_now_confirm": add_now_confirm1,
                    "total_confirm": total_confirm1})


@app.route('/get_right1_data', methods=['GET', 'POST'])
def get_right1_data():
    def return_real(num):
        if num > 0:
            return num
        else:
            return 0

    res = gdfdb.get_right1_data()

    # prov_list = ["台湾", "上海", "香港", "北京", "河南", "广东", "云南", "吉林", "辽宁", "贵州", "湖北", "陕西", "浙江", "福建", "黑龙江", "山东", "江苏",
    #              "四川", "河北", "天津", "内蒙古", "广西", "湖南", "江西", "安徽", "新疆", "重庆", "甘肃", "山西", "海南", "宁夏", "青海", "澳门", "西藏"]
    # city_list1, now_confirm1, add_confirm1, total_confirm1 = [], [], [], []
    # for i in prov_list:
    #     city_list, now_confirm, add_confirm, total_confirm = [], [], [], []
    #     for j in res:
    #         if i == j[0]:
    #             city_list.append(j[1])
    #             # now_confirm.append(int(j[2]))
    #             # add_confirm.append(int(j[3]))
    #             # total_confirm.append(int(j[4]))
    #             now_confirm.append(return_real(int(j[2])))
    #             add_confirm.append(return_real(int(j[3])))
    #             total_confirm.append(return_real(int(j[4])))
    #     city_list1.append(city_list)
    #     now_confirm1.append(now_confirm)
    #     add_confirm1.append(add_confirm)
    #     total_confirm1.append(total_confirm)
    #
    # return jsonify({"prov_name": prov_list, "city_name": city_list1, "now_confirm": now_confirm1, "add_confirm": add_confirm1, "total_confirm": total_confirm1})

    prov_list = ["台湾", "上海", "香港", "北京", "河南", "广东", "云南", "吉林", "辽宁", "贵州", "湖北", "陕西", "浙江", "福建", "黑龙江", "山东", "江苏",
                 "四川", "河北", "天津", "内蒙古", "广西", "湖南", "江西", "安徽", "新疆", "重庆", "甘肃", "山西", "海南", "宁夏", "青海", "澳门", "西藏"]
    data = []
    for i in prov_list:
        data2 = []
        for j in res:
            if i == j[0]:
                data1 = [j[1], return_real(int(j[2])), return_real(int(j[3])), return_real(int(j[4]))]
                data2.append(data1)
        data.append(data2)
    return jsonify({"prov_name": prov_list, "data": data})


@app.route('/get_right2_data', methods=['GET', 'POST'])
def get_right2_data():
    res = gdfdb.get_right1_data()

    prov_list = ["台湾", "上海", "香港", "北京", "河南", "广东", "云南", "吉林", "辽宁", "贵州", "湖北", "陕西", "浙江", "福建", "黑龙江", "山东", "江苏",
                 "四川", "河北", "天津", "内蒙古", "广西", "湖南", "江西", "安徽", "新疆", "重庆", "甘肃", "山西", "海南", "宁夏", "青海", "澳门", "西藏"]

    data = []
    for i in prov_list:
        now_confirm, add_confirm, total_confirm = [], [], []
        for j in res:
            if i == j[0]:
                now_confirm.append({"name": j[1], "value": j[2]})
                add_confirm.append({"name": j[1], "value": j[3]})
                total_confirm.append({"name": j[1], "value": j[4]})
        data.append(
            {"prov_name": i, "now_confirm": now_confirm, "add_confirm": add_confirm, "total_confirm": total_confirm})

    return jsonify(data)


@app.route("/get_left2_data", methods=['GET', 'POST'])
def get_left2_data():
    data = gdfdb.get_left2_data()
    # end_update_time, province, city, county, community, type
    details = []
    risk = []
    # end_update_time = data[0][0]
    for a, b, c, d, e, f in data:
        risk.append(f)
        details.append(f"{b}\t{c}\t{d}\t{e}")
    return jsonify({"risk": risk, "details": details})


@app.route('/get_bottom_data', methods=['GET', 'POST'])
def get_bottom_data():
    res = gdfdb.get_bottom_data()
    return jsonify({"prov_list": res[0], "date": res[1], "add_confirm": res[2]})


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='5001') # 当部署到服务器时这里更改为 host='10.0.12.4' port='8080'
