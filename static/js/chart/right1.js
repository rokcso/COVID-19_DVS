var myChartRight1 = echarts.init(document.getElementById("right-1"));

var myChartRight1Option = {
  title: {
    text: '全国各地区现有/新增/累计确诊数据',
    textStyle: {
      color: '#ffffff'
    }
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
  dataset: [{
      dimensions: ['city_name', 'now_confirm', 'add_confirm', 'total_confirm'],
      source: []
    },
    // {
    //   transform: {
    //     type: 'sort',
    //     config: { dimension: 'now_confirm', order: 'asc' }
    //   }
    // }
  ],
  xAxis: {
    type: 'category',
    // axisLabel: { interval: 0, rotate: 30 }
  },
  yAxis: {
    // type: 'category',
    // axisLabel: { interval: 0, rotate: 30 }
  },
  series: [{
      name: '现有确诊',
      type: 'bar',
      // encode: { x: 'now_confirm', y: 'city_name' },
      encode: {
        x: 'city_name',
        y: 'now_confirm'
      },
      // datasetIndex: 1
    },
    {
      name: '新增确诊',
      type: 'bar',
      // encode: { x: 'add_confirm', y: 'city_name' },
      encode: {
        x: 'city_name',
        y: 'add_confirm'
      },
      // datasetIndex: 1
    },
    {
      name: '累计确诊',
      type: 'bar',
      // encode: { x: 'total_confirm', y: 'city_name' },
      encode: {
        x: 'city_name',
        y: 'total_confirm'
      },
      // datasetIndex: 1
    }
  ]
};

// var myChartRight1Option = {
//     title: {
//         text: '全国现有/新增/累计确诊 Top 地区',
//         textStyle: {
//           color: '#ffffff'
//         }
//     },
//     tooltip: {
//         trigger: 'axis',
//         axisPointer: {
//           type: 'shadow'
//         }
//       },
//     legend: {
//         data: ['现有确诊', '新增确诊', '累计确诊'],
// 		left: 0,
// 		top: 20,
//         selected: {
//             '现有确诊': true,
//             '新增确诊': false,
//             '累计确诊': false
//         },
//         selectedMode: 'single'
//     },
//     grid: {
//         left: '3%',
//         right: '4%',
//         bottom: '3%',
//         containLabel: true
//       },
//       xAxis: {
//         type: 'value',
//         boundaryGap: [0, 0.01]
//       },
//       yAxis: {
//         type: 'category',
//         data: []
//       },
//       series: [
//         {
//           name: '现有确诊',
//           type: 'bar',
//           data: []
//         },
//         {
//           name: '新增确诊',
//           type: 'bar',
//           data: []
//         },
//         {
//           name: '累计确诊',
//           type: 'bar',
//           data: []
//         }
//       ]
// };

myChartRight1.setOption(myChartRight1Option)