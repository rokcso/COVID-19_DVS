var myChartLeft1 = echarts.init(document.getElementById("left-1"));

var myChartLeft1Option = {
	title: {
		text: '全国疫情变化趋势',
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
            '现有确诊': false,
            '新增确诊': true,
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
		  data: []
		},
		{
		  name: '新增确诊',
		  type: 'line',
		  stack: 'Total',
		  areaStyle: {},
		  emphasis: {
			focus: 'series'
		  },
		  data: []
		},
		{
		  name: '累计确诊',
		  type: 'line',
		  stack: 'Total',
		  areaStyle: {},
		  emphasis: {
			focus: 'series'
		  },
		  data: []
		}
	  ]
};

myChartLeft1.setOption(myChartLeft1Option);