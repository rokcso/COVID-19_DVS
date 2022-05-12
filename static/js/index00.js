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
            console.log("API /get_middle_data success!")
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


function getLeft1FirstData() {
    $.ajax({
        url: "/get_left1_first_data",
        type: "POST",
        timeout: "10000",
        success: function(data) {
            console.log("API /get_left1_first_data success!")
            res = data;
            myChartLeft1Option.xAxis[0].data = res["date"];
            myChartLeft1Option.series[0].data = res["now_confirm"];
            myChartLeft1Option.series[1].data = res["add_now_confirm"];
            myChartLeft1Option.series[2].data = res["total_confirm"];
            myChartLeft1.setOption(myChartLeft1Option);
            console.log("setOption final");
        },
        error: function(){
            console.log("API /get_left1_first_data error!")
        }
    });
}


function getLeft1Data() {
    myChartMiddle.on('click', function(e) {
        $.ajax({
            url: "/get_left1_data",
            type: "POST",
            timeout: "10000",
            success: function(data) {
                console.log("API /get_left1_data success!")
                res = data
                myChartLeft1Option.xAxis[0].data = res["date"];
                function clickWhere(point) {
                    for (var i = 0; i < res["prov_name"].length; i++) {
                        if (point == res["prov_name"][i]) {
                            return i;
                        }
                    }
                };
                flag = clickWhere(e.name);
                // console.log(e.name);
                // console.log(flag);
                myChartLeft1Option.series[0].data = res["now_confirm"][flag];
                myChartLeft1Option.series[1].data = res["add_now_confirm"][flag];
                myChartLeft1Option.series[2].data = res["total_confirm"][flag];
                myChartLeft1Option.title.text = res["prov_name"][flag] + '疫情变化趋势';
                myChartLeft1.setOption(myChartLeft1Option);
            },
            error: function(){
                console.log("API /get_left1_data error!")
            }
        })
    })
    
};


// function getRight1Data() {
//     myChartMiddle.on('click', function(e){
//         $.ajax({
//             url: "/get_right1_data",
//             type: "POST",
//             timeout: "10000",
//             success: function(data) {
//                 res = data;
//                 console.log(res)
//                 function clickWhere(point) {
//                     for (var i = 0; i < res["prov_name"].length; i++) {
//                         if (point ==  res["prov_name"][i]) {
//                             return i;
//                         }
//                     }
//                 }
//                 flag = clickWhere(e.name);
//                 myChartRight1Option.title.text = res["prov_name"][flag] + "现有/新增/累计确诊 Top 地区";
//                 myChartRight1Option.yAxis.data = res["city_name"][flag];
//                 myChartRight1Option.series[0].data = res["now_confirm"][flag];
//                 myChartRight1Option.series[1].data = res["add_confirm"][flag];
//                 myChartRight1Option.series[2].data = res["total_confirm"][flag];
//                 myChartRight1.setOption(myChartRight1Option)
//             },
//             error: function() {
//                 console.log("API /get_right1_data error!")
//             }
//         })
//     })
// };

function getRight1Data() {
    myChartMiddle.on('click', function(e){
        $.ajax({
            url: "/get_right1_data",
            type: "POST",
            timeout: "10000",
            success: function(data) {
                console.log("API /get_right1_data success!")
                res = data;
                // console.log(res)
                function clickWhere(point) {
                    for (var i = 0; i < res["prov_name"].length; i++) {
                        if (point ==  res["prov_name"][i]) {
                            return i;
                        }
                    }
                }
                flag = clickWhere(e.name);
                myChartRight1Option.title.text = res["prov_name"][flag] + "各地区现有/新增/累计确诊数据";
                myChartRight1Option.dataset[0].source = res["data"][flag]
                myChartRight1.setOption(myChartRight1Option)
            },
            error: function() {
                console.log("API /get_right1_data error!")
            }
        })
    })
};



setInterval(getDataUpdateTime, 1000);
getMiddleData();
getRight1Data();
getLeft1Data();
// getLeft1FirstData();