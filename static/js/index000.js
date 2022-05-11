function getDataUpdateTime() {
    $.ajax({
        url: "/get_data_update_time",
        type: "POST",
        timeout: "10000",
        success: function (data) {
            $("#top3").html(data)
        },
        error: function () {
            console.log("API /get_data_update_time error!")
        }
    })
}

function getMiddle1Num() {
    $.ajax({
        url: "/get_middle1_num",
        type: "POST",
        timeout: "10000",
        success: function (data) {
            $("#num1_1").html(data["confirm_now"]);
            $("#add1_1 span").html(data["confirm_add"]);
            $("#num1_2").html(data["suspect"]);
            $("#add1_2 span").html(data["suspect_add"]);
            $("#num1_3").html(data["heal"]);
            $("#add1_3 span").html(data["heal_add"]);
            $("#num1_4").html(data["dead"]);
            $("#add1_4 span").html(data["dead_add"]);
        },
        error: function () {
            console.log("API /get_middle1_num error!")
        }
    })
}

function get_middle2_data() {
    $.ajax({
        url: "/get_middle2_data",
        type: "POST",
        timeout: "10000",
        success: function (data) {
            res = data.data;
            console.log(res);
            myChart_middle2_option.series[0].data = res;
            myChart_middle2.setOption(myChart_middle2_option)
        },
        error: function (xhr, type, errorThrown) {
            console.log("API /get_middle2_data error!")
        }
    })
}

function getLeft1Data() {
    myChart_middle2.on('click', function (e) {
        $.ajax({
            url: "/get_left1_data",
            type: "POST",
            timeout: "10000",
            success: function (data) {
                res = data.data
                // console.log(res);
                var xData = [];
                var yData = [];
                // 判断点击位置从而选择数据
                function clickWhere(point) {
                    for (var i = 0; i < res.length; i++) {
                        if (point == res[i].prov_name) {
                            return i;
                        }
                    }
                };
                // 解析数据
                res1 = res[clickWhere(e.name)];
                console.log(res1);
                $.each(res1.data, function (index, item) {
                    xData.push(item.name);
                    yData.push(item.value);
                });
                myChart_left1.setOption({
                    title: {
                        text: res1.prov_name + '现存/新增确诊人数',
                    },
                    xAxis: {
                        data: xData
                    },
                    yAxis: {},
                    series: [{
                        type: 'bar',
                        data: yData
                    }]
                })
            },
            error: function () {
                console.log("API /get_left1_data error!")
            }
        })
    })
}

function getRight1Data() {

}

// setInterval(getDataUpdateTime, 1000)
getDataUpdateTime();
getMiddle1Num();
get_middle2_data();
getLeft1Data();
getRight1Data();