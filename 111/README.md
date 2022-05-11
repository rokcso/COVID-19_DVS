# 帮助文档（README.md）

![当前程序版本](https://img.shields.io/badge/version-1.0-lightgrey.svg)
![Python3版本](https://img.shields.io/badge/Python-3.8.2-informational.svg)
![ECharts版本](https://img.shields.io/badge/ECharts-2.0-critical.svg)
![CentOS版本](https://img.shields.io/badge/CentOS-7.7-purple.svg)
![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)

## 项目简介

本项目是本人本科的毕设项目，也是开源的第一个项目，因能力、时间、精力有限，因此项目相对小型，希望随着后续的学习能够开源更好的项目。

## 项目部分截图

![covid19国内模块部分截图](https://qiniuyun.zhanqingheng.com/2020-06-07-18-40-59-202067.png)

![covid19国外模块部分截图](https://qiniuyun.zhanqingheng.com/2020-06-07-18-41-40-202067.png)


## 项目开发背景

新冠疫情（`COVID-19`）爆发以来，丁香园、百度、腾讯、北大可视化团队等相继上线一些疫情数据可视化网站。因为本人是计算机专业学生，加上临近毕业需要做毕设，所以就想学习一下`Python`，学以致用地开发类似网站，在抗击疫情的过程中尽到自己的绵薄之力。

项目已部署在云服务器中，点击[疫情吹哨系统](https://covid19.zhanqingheng.com)即可访问。这里简要编写此项目介绍，我在个人博客网站[太阳照常升起](https://zhanqingheng.com)中有详细讲解，欢迎前往浏览。

仅以此项目致敬那些奋战到一线的医护人员。

## 项目开发及部署过程

### 前期准备阶段

1.学习`Python`、爬虫、`Linux`的相关知识

2.在知乎、B站中搜索并学习“用`Python`做疫情可视化网站”的相关知识

### 开发阶段

1.安装`PyCharm`、`Python3`、`pip`、`Jupyter Notebook`、`MySQL`

2.编写爬虫（利用`Jupyter Notebook`在浏览器中调试）爬取数据并处理

3.根据爬取的数据建库建表并存储数据

4.利用`Flask`框架搭建简单后台（根据展示条件查询数据并转换数据格式准备传输到前台）

5.根据开发需要边写边扩展类库

6.前台使用`HTML5`+`CSS`+`JS`+`jQuery`搭建页面

7.学习并使用适当`ECharts`可视化工具

8.利用`AJAX`将后台和前台连通，并把后台传输的数据放在`ECharts`中

9.完成数据从爬取、处理、保存到前端根据需要查询并可视化展示不同数据

### 部署阶段

1.设置云服务器的基本环境

2.安装`MySQL`并设置云端账号密码和远程登录账号密码

3.服务器默认`Python2`，所以安装`Python3`和`pip`。并利用`pip`将项目所需依赖进行安装

4.因爬虫程序需要，所以在云服务器中安装`Chrome`和对应版本的`ChromeDriver`

5.将项目文件上传到云服务器中

6.安装`Nginx`并设置项目路径、网站域名，作为网站代理

7.安装`Gunicorn`并挂载到后台即可从外网访问到网站

8.利用云服务器`Linux`的`crontab`制定爬虫程序的定时运行

9.在`Nginx`配置文件中设置`gzip`进行项目的压缩，加快访问速度

![COVID19开发及部署阶段图片](https://qiniuyun.zhanqingheng.com/2020-06-07-16-47-50-202067.png)

## 仓库目录结构描述

### covid19文件夹

`covid19`文件夹中即项目的源代码，其中的`code`文件夹是后台代码，`code`下的`controller`为核心代码，里面是项目的启动程序；`DB`下的为查询数据库代码；`spider`为爬虫程序文件夹，里面分别有不同接口的爬虫程序、疫情热搜的爬虫程序和`windows`和`Linux`端的`chromedriver`程序。

`static`文件夹中`css`为前端布局；`image`为网站图标；`js`文件夹下的`AJAX`是前后端数据传输的`AJAX`程序；`ECharts`是自己使用并自定义的`ECharts`工具；`province`是项目中所有省份的js效果图文件；`themes`是`ECharts`的不同颜色主题；`tool`是引用的`ECharts`、`china`、`world`、`jquery`的`js`文件。

`web`文件夹中是两个前端页面`china.html`和`world.html`。

### img文件夹为编写md中使用的图片

### 16张数据表.md文件为此项目所需的数据表创建代码

### LICENSE 开源许可证文档

### README.md为本解释性文档


## 如何食用此项目

1.在本地安装`PyCharm`、`Python3`、`pip`、项目依赖包

2.安装并使用数据库代码创建表创建库

3.安装浏览器对应版本`chromedriver`程序

4.运行`spider`文件夹中的爬虫程序存储数据

5.运行`main.py`即可在本地5000端口运行出此项目


## 版本内容更新

2020.6.6上线`v1.0`，因学业原因，只能后续有时间、有机会才能更新

## License

[MIT License](https://github.com/zhanqingheng/COVID-19/blob/master/LICENSE)
