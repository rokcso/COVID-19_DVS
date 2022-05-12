function getDataUpdateTime() {
    $.ajax({
        url: "/get_data_update_time",
        type: "POST",
        timeout: "10000",
        success: function (data) {
            $("#update-time").html(data)
        },
        error: function () {
            console.log("API /get_data_update_time error!")
        }
    })
};


function getMiddleData() {
    $.ajax({
        url: "/get_middle_data",
        type: "POST",
        timeout: "10000",
        success: function(data){
            myChartMiddleOption.series[0].data = data["now_confirm"];
            myChartMiddleOption.series[1].data = data["add_now_confirm"];
            myChartMiddleOption.series[2].data = data["total_confirm"];
            myChartMiddle.setOption(myChartMiddleOption);
        },
        error: function(){
            console.log("API /get_middle_data error!")
        }
    })
};


function getLeft1Data() {
    $.ajax({
        url: "/get_left1_data",
        type: "POST",
        timeout: "10000",
        success: function(data) {
            myChartLeft1Option.xAxis[0].data = data["date"];
            myChartLeft1Option.series[0].data = data["now_confirm"];
            myChartLeft1Option.series[1].data = data["add_now_confirm"];
            myChartLeft1Option.series[2].data = data["total_confirm"];
            myChartLeft1.setOption(myChartLeft1Option);
        },
        error: function(){
            console.log("API /get_left1_data error!")
        }
    })
};


function getRight1Data() {
    $.ajax({
        url: "/get_left1_data",
        type: "POST",
        timeout: "10000",
        success: function(data) {
            myChartLeft1Option.xAxis[0].data = data["date"];
            myChartLeft1Option.series[0].data = data["now_confirm"];
            myChartLeft1Option.series[1].data = data["add_now_confirm"];
            myChartLeft1Option.series[2].data = data["total_confirm"];
            myChartLeft1.setOption(myChartLeft1Option);
        },
        error: function(){
            console.log("API /get_left1_data error!")
        }
    })
};



setInterval(getDataUpdateTime, 1000);
getMiddleData();
getLeft1Data();
getRight1Data();