## 备忘信息

> https://www.base64.pro/

### 云服务器

公网 IP --> `124.221.238.251`

pwd --> `V2FyaW5nQDY3NjkkaHU=`

MySQL --> `QDY3NjlAbXlzcWwmaHU=`

### 数据源

https://news.qq.com/zt2020/page/feiyan.htm#/

### 创建 details 表

> update_time, prov_name, prov_now_confirm, prov_today_confirm, prov_total_confirm, prov_total_heal, prov_total_dead, city_name, city_now_confirm, city_today_confirm, city_total_confirm, city_total_heal, city_total_dead

```mysql
CREATE TABLE `details` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `update_time` datetime DEFAULT NULL COMMENT '数据更新时间',
    `prov_name` varchar(50) DEFAULT NULL COMMENT '省名',
    `prov_now_confirm` int(11) DEFAULT NULL COMMENT '现存确诊',
    `prov_today_confirm` int(11) DEFAULT NULL COMMENT '当日新增确诊',
    `prov_total_confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
    `prov_total_heal` int(11) DEFAULT NULL COMMENT '累计治愈',
    `prov_total_dead` int(11) DEFAULT NULL COMMENT '累计死亡',
    `city_name` varchar(50) DEFAULT NULL COMMENT '市名',
    `city_now_confirm` int(11) DEFAULT NULL COMMENT '现存确诊',
    `city_today_confirm` int(11) DEFAULT NULL COMMENT '当日新增确诊',
    `city_total_confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
    `city_total_heal` int(11) DEFAULT NULL COMMENT '累计治愈',
    `city_total_dead` int(11) DEFAULT NULL COMMENT '累计死亡',
    PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
```