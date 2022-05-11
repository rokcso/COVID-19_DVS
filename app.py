from flask import Flask, jsonify
from flask import render_template
import utils

# 初始化一个 Python Flask App 对象
app = Flask(__name__)


# 创建一个路由，路径在根目录「/」下，允许的请求方式有 GET、POST
@app.route('/', methods=['GET', 'POST'])
def root():
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
    return utils.get_data_update_time()


# 创建获取 middle1 位置的数字数据的路由
@app.route('/get_middle1_num', methods = ['GET', 'POST'])
def get_middle1_num():
    """
    返回 middle1 位置的数字数据：
    :return:
    """
    return utils.get_middle1_num()


@app.route('/get_middle2_data', methods=['GET', 'POST'])
def get_middle2_data():
    """
    返回 middle2 位置的数据：
    :return:
    """
    res = utils.get_middle2_data()
    res1 = []
    for item in res:
        res1.append({"name": item[0], "value": int(item[1])})
    res2 = jsonify({"data": res1})
    return res2


@app.route('/get_left1_data', methods=['GET', "POST"])
def get_left1_data():
    """
    :return:
    """
    res = utils.get_left1_data()
    res1 = []
    for item in res:
        res1.append({"prov_name": item[0], "data": [{"name": "现存确诊", "value": item[1]}, {"name": "当日新增", "value": item[2]}]})
    res2 = jsonify({"data": res1})
    return res2


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='5021')
