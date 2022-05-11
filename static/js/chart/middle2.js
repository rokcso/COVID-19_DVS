var myChart_middle2 = echarts.init(document.getElementById('middle2'));

var myChart_middle2_option = {
    title: {
        text: '全国现有确诊',
        subtext: '',
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        data: ['现存确诊', '新增确诊', '累计治愈', "累计死亡"],
        left: 20,
        top: 80,
        selected: {
            '现存确诊': true,
            '新增确诊': false,
            '累计治愈': true,
            '累计死亡': false
        },
        selectedMode: "single",
        textStyle: {
            color: '#000',
            fontSize: 18
        }
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{
                start: 0,
                end: 0
            },
            {
                start: 1,
                end: 9
            },
            {
                start: 10,
                end: 99
            },
            {
                start: 100,
                end: 999
            },
            {
                start: 1000,
                end: 9999
            },
            {
                start: 10000
            }
        ],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: "现存确诊",
        type: 'map',
        roam: false,
        zoom: 1.2,
        mapType: 'china',
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "新增确诊",
        type: 'map',
        roam: false,
        mapType: 'china',
        zoom: 1.2,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "累计治愈",
        type: 'map',
        roam: false,
        mapType: 'china',
        zoom: 1.2,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "累计死亡",
        type: 'map',
        mapType: 'china',
        zoom: 1.2,
        roam: false,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }]
};

myChart_middle2.setOption(myChart_middle2_option);

// var myChart_middle2 = echarts.init(document.getElementById('middle2'));

// var myChart_middle2_option = {
//   title: {
//     text: '全国地图疫情地图',
//     left: 'center'
//   },
//   tooltip: {
//     trigger: 'item',
//     formatter: '{b}<br/>{c} (p / km2)'
//   },
//   toolbox: {
//     show: true,
//     orient: 'vertical',
//     left: 'right',
//     top: 'center',
//     feature: {
//       restore: {}
//     }
//   },
//   visualMap: {
//     min: 800,
//     max: 50000,
//     text: ['High', 'Low'],
//     realtime: false,
//     calculable: true,
//     inRange: {
//       color: ['lightskyblue', 'yellow', 'orangered']
//     }
//   },
//   series: [
//     {
//       name: '全国地图疫情地图',
//       type: 'map',
//       map: '全国',
//       label: {
//         show: true
//       },
//       data: [{"name":"上海市","value":6232},{"name":"北京市","value":10},{"name":"四川省","value":29},{"name":"\u5317\u4eac","value":586},{"name":"\u53f0\u6e7e","value":342610},{"name":"\u5409\u6797","value":320},{"name":"\u56db\u5ddd","value":51},{"name":"\u5929\u6d25","value":0},{"name":"\u5b81\u590f","value":0},{"name":"\u5b89\u5fbd","value":5},{"name":"\u5c71\u4e1c","value":58},{"name":"\u5c71\u897f","value":13},{"name":"\u5e7f\u4e1c","value":210},{"name":"\u5e7f\u897f","value":12},{"name":"\u65b0\u7586","value":0},{"name":"\u6c5f\u82cf","value":16},{"name":"\u6c5f\u897f","value":65},{"name":"\u6cb3\u5317","value":10},{"name":"\u6cb3\u5357","value":133},{"name":"\u6d59\u6c5f","value":521},{"name":"\u6d77\u5357","value":16},{"name":"\u6e56\u5317","value":2},{"name":"\u6e56\u5357","value":23},{"name":"\u6fb3\u95e8","value":0},{"name":"\u7518\u8083","value":0},{"name":"\u798f\u5efa","value":54},{"name":"\u897f\u85cf","value":0},{"name":"\u8d35\u5dde","value":1},{"name":"\u8fbd\u5b81","value":28},{"name":"\u91cd\u5e86","value":6},{"name":"\u9655\u897f","value":0},{"name":"\u9752\u6d77","value":14},{"name":"\u9999\u6e2f","value":261328},{"name":"\u9ed1\u9f99\u6c5f","value":65}]
//     }
//   ]
// }

// $.get('../static/chinaJson/100000_full.json', function (geoJson) {
//   echarts.registerMap('全国', geoJson);
//   myChart_middle2.setOption(myChart_middle2_option);
// });