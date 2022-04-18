from flask import Flask
from flask import render_template
import utils
import spiders

# 初始化一个 Python Flask App 对象
app = Flask(__name__)

# 创建一个路由，路径在根目录「/」下，允许的请求方式有 GET、POST
@app.route('/', methods = ['GET', 'POST'])
def root():
    """
    返回一个 HTML 模板文件
    :return: index.html
    """
    return render_template('index.html')

# 创建获取数据更新时间的路由
@app.route('/get_data_update_time', methods = ['GET', 'POST'])
def get_data_update_time():
    """
    返回数据更新时间：
    - 'Data updated in 2022-04-18 12:34 (2h42m ago)'
    :return: data_update_time
    """
    return utils.get_data_update_time()

# 创建获取 middle1 位置的数字数据的路由
@app.route('/get_middle_num', methods = ['GET', 'POST'])
def get_data():
    """
    返回 middle1 位置的数字数据：
    - 现存确诊人数
    - 今日新增确诊人数
    - 累计确诊人数
    - 累计治愈人数
    - 累计死亡人数
    :return: sum(city_now_confirm), sum(city_today_confirm), sum(city_total_confirm), sum(city_total_heal), sum(city_total_dead)
    """
    return utils.get_middle_num()

# 创建获取 middle2 的数据的路由
@app.route('/get_middle2_data', methods = ['GET', 'POST'])
def get_middle2_data():
    """
    返回 middle2 位置的数据：
    - 省份名称
    - 省份现存确诊人数
    :return: prov_name, prov_now_confirm
    """
    return utils.get_middle2_data()

@app.route('/get_left1_data', methods = ['GET', 'POST'])
def get_left1_data():
    """
    返回 left1 位置的数据
    :return:
    """
    return utils.get_left1_data()

if __name__ == '__main__':
    spiders.main()
    app.run(debug=False, host='127.0.0.1', port='5006')