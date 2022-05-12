var myChartRight1 = echarts.init(document.getElementById("right-1"));

var myChartRightOption = {
    title: {
        text: '全国现有/新增/累计确诊 Top 城市'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
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
        selectedMode: 'single'
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
      },
      yAxis: {
        type: 'category',
        data: []
      },
      series: [
        {
          name: '现有确诊',
          type: 'bar',
          data: [18203, 23489, 29034, 104970, 131744, 630230]
        },
        {
          name: '新增确诊',
          type: 'bar',
          data: [19325, 23438, 31000, 121594, 134141, 681807]
        },
        {
          name: '累计确诊',
          type: 'bar',
          data: [19325, 23438, 31000, 121594, 134141, 681807]
        }
      ]
};

myChartRight1.setOption(myChartRightOption)