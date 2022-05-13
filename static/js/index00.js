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
            // console.log(data)
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


// function getLeft2Data() {
//     $.ajax({
//         url: "/get_left2_data",
//         type: "POST",
//         timeout: "10000",
//         success: function(data) {
//             var update_time = data.update_time
//             var details = data.details
//             var risk = data.risk
//             //  $("#l2 .ts").html("截至时间：" + update_time)
//             var s =""
//             for(var i in details){
//                 if (risk[i] == "高风险"){
//                      s += "<li><span class='high_risk'>高风险\t\t</span>"+ details[i] + "</li>"
//                 }else{
//                      s += "<li><span class='middle_risk'>中风险\t\t</span>"+ details[i] + "</li>"
//                 }
//             }
//              $("#risk_wrapper_li1 ul").html(s)
//             start_roll()
// 		},
// 		error: function(xhr, type, errorThrown) {
// 		}
//     })
// }


function getLeft2Data() {
    $.ajax({
        url: '/get_left2_data',
        type: 'POST',
        timeout: '10000',
        success: function(data) {
            var details = data.details;
            var risk = data.risk;
            // console.log(details);
            // console.log(risk);
            var h_num = 0;
            var m_num = 0;
            var falg = '';
            for (var i in details) {
                if (risk[i] == '高风险') {
                    falg += "<li><span class='hight-risk'>高风险</span>" + details[i] + "</li>"
                    h_num = h_num + 1;
                } else {
                    falg += "<li><span class='middle-risk'>中风险</span>" + details[i] + "</li>"
                    m_num = m_num + 1;
                }
            };
            // console.log(falg);
            $("#left1-num1-num").html(h_num);
            $("#left1-num2-num").html(m_num);
            $("#risk_wrapper_li1 ul").html(falg);
            start_roll()
        },
        error: function() {
            console.log("API /get_left2_data error!")
        }
    })
};


setInterval(getDataUpdateTime, 1000);
getMiddleData();
getRight1Data();
getLeft1Data();
getLeft2Data();
// getLeft1FirstData();