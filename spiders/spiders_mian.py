import get_day_data
import get_details_data
import get_risk_area_data
import get_prov_day_data

if __name__ == "__main__":
    get_day_data.update_china_day_list()  # 更新全国日更历史数据
    get_details_data.update_china_details()  # 更新全国基础疫情数据
    get_details_data.update_prov_details()  # 更新省级基础疫情数据
    get_details_data.update_city_details()  # 更新市级基础疫情数据
    get_risk_area_data.update_risk_area_data()  # 更新风险地区数据
    # get_prov_day_data.update_prov_day_data()  # 更新省份日更历史数据，注意：最好每天 00:01 更新
