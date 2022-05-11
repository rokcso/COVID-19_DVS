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


setInterval(getDataUpdateTime, 1000);
getMiddleData();