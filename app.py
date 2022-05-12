
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


@app.route('/index01', methods=['GET', 'POST'])
def index01():
    """
    返回一个 HTML 模板文件
    :return: 
    """
    return render_template('index01.html')


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
    day_data = []
    data = {}
    for i in res:
        for j in res:
            day_data.append({"date": str(j[0])[5:10], "now_confirm": j[2], "add_now_confirm": j[3], "total_confirm": j[4]})
        data[i[1]] = day_data
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='5026')
