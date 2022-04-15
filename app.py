from flask import Flask
from flask import render_template
import utils

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def root():
    """
    首页
    :return: index.html
    """
    return render_template('index.html')

@app.route('/get_local_time', methods = ['GET', 'POST'])
def get_time():
    """
    获取本地时间并返回
    :return: local_time
    """
    return utils.get_local_time()

@app.route('/get_data_update_time', methods = ['GET', 'POST'])
def get_data_update_time():
    """
    获取数据更新时间
    :return: data_update_time
    """
    return utils.get_data_update_time()

@app.route('/get_middle_num', methods = ['GET', 'POST'])
def get_data():
    """
    获取中间数字
    :return: middle num
    """
    return utils.get_middle_num()

@app.route('/get_middle2_data', methods = ['GET', 'POST'])
def get_middle2_data():
    """
    获取中间第二个图表的数据，地图
    :return:
    """
    return utils.get_middle2_data()

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='5000')