var myChartBottom = echarts.init(document.getElementById("bottom"));

const prov_list = ['湖北', '四川', '上海'];

const day_list = ['04.29', '04.30', '05.01', '05.02', '05.03', '05.04', '05.05', '05.06', '05.07', '05.08', '05.09', '05.10', '05.11', '05.12'];

const data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], 
              [1, 0, 3], [1, 1, 4], [1, 2, 6], [1, 3, 4], [1, 4, 4], [1, 5, 3], [1, 6, 3], [1, 7, 2], [1, 8, 5], [1, 9, 7], [1, 10, 0], [1, 11, 0], [1, 12, 0], [1, 12, 0], [1, 14, 0], 
              [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 5], [2, 5, 2], [2, 6, 2], [2, 7, 6], [2, 8, 9], [2, 9, 11], [2, 10, 6], [2, 11, 7], [1, 12, 8], [1, 13, 12], [1, 14, 5]]
              .map(function (item) {
    return [item[1], item[0], item[2] || '-'];
});

// console.log(data);

var myChartBottomOption = {
    title: {
        text: '近 60 天疫情爆发 TOP7 省份新增确诊趋势',
        textStyle: {
            color: '#ffffff'
        }
    },
    tooltip: {
        position: 'top'
      },
    grid: {
        height: '72%',
        top: 30,
        right: 15,
        left: 40
      },
      xAxis: {
        type: 'category',
        data: day_list,
        splitArea: {
          show: true
        }
      },
      yAxis: {
        type: 'category',
        data: prov_list,
        splitArea: {
          show: true
        }
      },
      visualMap: {
        min: 0,
        max: 1000,
        calculable: false,
        orient: 'horizontal',
        // right: 0,
        top: 0,
        left: 350
      },
      series: [
        
        {
            name: '新增确诊',
            type: 'heatmap',
            data: data,
            label: {
              show: true
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
      ]
};

myChartBottom.setOption(myChartBottomOption);