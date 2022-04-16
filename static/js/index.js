function getLocalTime() {
    // 获取时间
    $.ajax({
        url: "/get_local_time",
        type: "POST",
        timeout: "10000",
        success:function(data) {
            $("#time").html(data)
        },
        error:function() {
            alert("API /get_local_time error!")
        }
    })
}

function getMiddleNum() {
    $.ajax({
        url: "/get_middle_num",
        type: "POST",
        timeout: "10000",
        success:function(data){
            $(".middle1_num").eq(0).html(data["now_confirm"]);
            $(".middle1_num").eq(1).html(data["today_confirm"]);
            $(".middle1_num").eq(2).html(data["total_confirm"]);
            $(".middle1_num").eq(3).html(data["total_heal"]);
            $(".middle1_num").eq(4).html(data["total_dead"])
        },
        error:function(){
            console.log("API /get_middle_num error!")
        }
    })
}

function getMiddle2Data() {
    $.ajax({
        url: "/get_middle2_data",
        type: "POST",
        timeout: "10000",
        success:function(data) {
            console.log(data);
            option.series[0].data = data.data;
            myChart.setOption(option)
        },
        error:function() {
            console.log("API /get_middle2_data error!")
        }
    })
}

function getDataUpdateTime() {
    $.ajax({
        url: "/get_data_update_time",
        type: "POST",
        timeout: "10000",
        success:function(data) {
            $("#time").html(data)
        },
        error:function() {
            console.log("API /get_data_update_time error!")
        }
    })
}

// setInterval(getLocalTime, 1000)
// getLocalTime()
getMiddleNum()
getMiddle2Data()
getDataUpdateTime()