var myChartLeft1 = echarts.init(document.getElementById("left-1"));

var myChartLeft1Option = {
	title: {
		text: '全国疫情变化趋势'
	},
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'cross',
			label: {
				backgroundColor: '#6a7985'
			}
		}
	},
	legend: {
		data: ['现有确诊', '新增确诊', '累计确诊'],
		left: 0,
		top: 20
	},
	grid: {
		left: '3%',
		right: '4%',
		bottom: '3%',
		containLabel: true
	},
	xAxis: [
		{
		  type: 'category',
		  boundaryGap: false,
		  data: []
		}
	  ],
	  yAxis: [
		{
		  type: 'value'
		}
	  ],
	  series: [
		{
		  name: '现有确诊',
		  type: 'line',
		  stack: 'Total',
		  areaStyle: {},
		  emphasis: {
			focus: 'series'
		  },
		  data: [120, 132, 101, 134, 90, 230, 210]
		},
		{
		  name: '新增确诊',
		  type: 'line',
		  stack: 'Total',
		  areaStyle: {},
		  emphasis: {
			focus: 'series'
		  },
		  data: [220, 182, 191, 234, 290, 330, 310]
		},
		{
		  name: '累计确诊',
		  type: 'line',
		  stack: 'Total',
		  areaStyle: {},
		  emphasis: {
			focus: 'series'
		  },
		  data: [150, 232, 201, 154, 190, 330, 410]
		}
	  ]
};

myChartLeft1.setOption(myChartLeft1Option);