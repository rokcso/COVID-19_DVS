// var myChartRight2 = echarts.init(document.getElementById("right-2"));

myChartMiddle.on('click', function (e) {
    var myChartRight2 = echarts.init(document.getElementById("right-2"));
    var myChartRight2Option;
    var ROOT_PATH = '\\static\\chinaGeoJson';
    var url = ROOT_PATH + '\\' + e.name + '.json';
    // console.log(e.name);
    $.get(url, function (geoJson) {
        echarts.registerMap(e.name, geoJson);
        myChartRight2.setOption(
            (myChartRight2Option = {
                title: {
                    text: e.name + '疫情地图',
                    textStyle: {
                        color: '#ffffff'
                    }
                },
                tooltip: {
                    trigger: 'item'
                },
                visualMap: {
                    show: false,
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
                            end: 499
                        },
                        {
                            start: 500,
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
                    color: ['#de1f05', '#ff2736', '#ff6341', '#ffa577', '#ffcea0', '#ffe7b2', '#e2ebf4']
                },
                legend: {
                    data: ['现有确诊', '新增确诊', '累计确诊'],
                    // left: 0,
                    // bottom: 0,
                    x: 'left',
                    y: 'bottom',
                    orient: 'vertical',
                    selected: {
                        '现有确诊': false,
                        '新增确诊': false,
                        '累计确诊': true
                    },
                    selectedMode: 'single',
                    textStyle: {
                        color: '#232323'
                    }
                },
                series: [{
                    name: '现有确诊',
                    type: 'map',
                    roam: true,
                    zoom: 1.2,
                    map: e.name,
                    label: {
                        show: true
                    },
                    data: [{name: '黄浦', value: 1235},
                    {'name': '徐汇', 'value': 1102},
                    {'name': '浦东', 'value': 1058},
                    {'name': '虹口', 'value': 940},
                    {'name': '静安', 'value': 887},
                    {'name': '杨浦', 'value': 835},
                    {'name': '闵行', 'value': 619},
                    {'name': '长宁', 'value': 522},
                    {'name': '宝山', 'value': 497},
                    {'name': '普陀', 'value': 475},
                    {'name': '崇明', 'value': 165},
                    {'name': '嘉定', 'value': 97},
                    {'name': '奉贤', 'value': 84},
                    {'name': '青浦', 'value': 57},
                    {'name': '松江', 'value': 50},
                    {'name': '金山', 'value': 9}
                ]
                },
                {
                    name: '新增确诊',
                    type: 'map',
                    roam: true,
                    zoom: 1.2,
                    map: e.name,
                    label: {
                        show: true
                    },
                    data: []
                },
                {
                    name: '累计确诊',
                    type: 'map',
                    roam: true,
                    zoom: 1.2,
                    map: e.name,
                    label: {
                        show: true
                    },
                    data: []
                }
            ]
            })
        );
    });

    $.ajax({
        url: 'get_right2_data',
        type: 'POST',
        timeout: '10000',
        success: function(data) {
            console.log("API /get_right2_data success!");
            res = data;
            // console.log(res);
            function clickWhere(point) {
                for (var i = 0; i < res.length; i++) {
                    if (point == res[i]["prov_name"]) {
                        return i;
                    }
                }
            };
            flag = clickWhere(e.name);
            console.log(res[flag]);
            myChartRight2Option.series[0].data = res[flag]["now_confirm"];
            myChartRight2Option.series[1].data = res[flag]["add_confirm"];
            myChartRight2Option.series[2].data = res[flag]["total_confirm"];
            myChartRight2.setOption(myChartRight2Option);
        },
        error: function() {
            console.log("API /get_right2_data error!")
        }
    })

});

// myChartRight2.setOption(myChartRight2Option);

