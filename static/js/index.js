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

function getMiddle1Num() {
    $.ajax({
        url: "/get_middle1_num",
        type: "POST",
        timeout: "10000",
        success:function(data){
            $("#num1_1").html(data["confirm_now"]);
            $("#add1_1 span").html(data["confirm_add"]);
            $("#num1_2").html(data["suspect"]);
            $("#add1_2 span").html(data["suspect_add"]);
            $("#num1_3").html(data["heal"]);
            $("#add1_3 span").html(data["heal_add"]);
            $("#num1_4").html(data["dead"]);
            $("#add1_4 span").html(data["dead_add"]);
        },
        error:function(){
            console.log("API /get_middle1_num error!")
        }
    })
}

function getMiddle2Data() {
    $.ajax({
        url: "/get_middle2_data",
        type: "POST",
        timeout: "10000",
        success:function(data) {
            optionMiddle2.series[0].data = data.data;
            chartMiddle2.setOption(optionMiddle2)
        },
        error:function() {
            console.log("API /get_middle2_data error!")
        }
    })
}

// setInterval(getDataUpdateTime, 1000)
getMiddle1Num()
getMiddle2Data()
getDataUpdateTime()