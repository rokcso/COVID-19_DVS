function getNum() {
    $.ajax({
        url: "/get_num",
        type: "POST",
        timeout: "10000",   
        success: function (data) {
            console.log("API /get_num success!");

            $("#num-0").html(data["now_local_confirm"]);
            $("#num-1").html(data["now_confirm"]);
            $("#num-2").html(data["total_confirm"]);
            $("#num-3").html(data["total_no_infect"]);
            $("#num-4").html(data["total_imported_case"]);
            $("#num-5").html(data["total_dead"]);

            $("#add-0 span").html(data["add_now_local_confirm"]);
            $("#add-1 span").html(data["add_now_confirm"]);
            $("#add-2 span").html(data["add_total_confirm"]);
            $("#add-3 span").html(data["add_total_no_infect"]);
            $("#add-4 span").html(data["add_total_imported_case"]);
            $("#add-5 span").html(data["add_total_dead"]);
        },
        error: function () {
            console.log("API /get_num error!");
        }
    })
}

function getDataUpdateTime() {
    $.ajax({
        url: "/get_data_update_time",
        type: "POST",
        timeout: "10000",
        success: function(data) {
            console.log("API /get_data_update_time success!");

            $("#update-time-1").html(data);
            $("#update-time-2").html(data);
        },
        error: function(){
            console.log("API /get_data_update_time error!");
        }
    })
}

getNum();
setInterval(getDataUpdateTime, 1000)
// getDataUpdateTime()