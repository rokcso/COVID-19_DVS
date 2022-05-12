var myChartMiddle = echarts.init(document.getElementById("middle"));

var myChartMiddleOption = {
    title: {
        text: '全国疫情地图',
        textStyle: {
            color: '#ffffff'
          }
    },
    tooltip: {
        trigger: 'item'
    },
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
        left: 0,
        top: 20,
        selected: {
            '现有确诊': true,
            '新增确诊': false,
            '累计确诊': false
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
        mapType: 'china',
        label: {
            show: true
        },
        data: [{name: "四川", value: 999}]
    },
    {
        name: '新增确诊',
        type: 'map',
        roam: true,
        zoom: 1.5,
        mapType: 'china',
        label: {
            show: true,
        },
        data: []
    }, {
        name: '累计确诊',
        type: 'map',
        roam: true,
        zoom: 1.5,
         mapType: 'china',
        label: {
            show: true,
        },
                    data: []
                }
            ]
};

myChartMiddle.setOption(myChartMiddleOption);