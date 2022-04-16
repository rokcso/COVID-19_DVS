from flask import Flask
from flask import render_template
import utils
import spiders

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def root():
    """
    首页
    :return: index.html
    """
    return render_template('index.html')

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

@app.route('/get_left1_data', methods = ['GET', 'POST'])
def get_left1_data():
    """
    获取左边第一个图标数据
    :return:
    """
    return utils.get_left1_data()

if __name__ == '__main__':
    # spiders.main()
    app.run(debug=False, host='127.0.0.1', port='5006')