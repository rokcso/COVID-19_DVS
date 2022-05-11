var myChart_left1 = echarts.init(document.getElementById('left1'));

var myChart_left1_option = {
    title: {
        text: '全国现存/新增确诊人数',
    },
    xAxis: {
		data: ['AA', 'BB', 'CC']
	},
	yAxis: {},
	series: [{
		type: 'bar',
		data: [12, 23, 34]
	}]
};

myChart_left1.setOption(myChart_left1_option);