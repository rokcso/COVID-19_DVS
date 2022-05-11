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


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='5008')
