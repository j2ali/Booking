$(document).ready(function () {
    $("#my-calendar").zabuto_calendar({
        action: function () {
            return myDateFunction(this.id, false);
        },
        action_nav: function () {
            return myNavFunction(this.id);
        }
    });

    var time;
    var date;

    $('td').on('click', function(){
        time = $(this).attr('time');
        date = $(this).attr('date');
    });

     $('#save_appointment').on('click', function(){
        var name = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var phone_number = document.getElementById("phone_number").value;
        nav(time, date, name, email, phone_number)
    });
});

function myDateFunction(id) {
    var date = $("#" + id).data("date");
    var dateList = date.split("-");
    var year = dateList[0];
    var month = dateList[1];
    var day = dateList[2];

    console.log(date)
    move(year, month, day)
    return true;
}

function move(year, month, day){
    window.location = "/reservations/available_appointments/?" + "year="+ year +
            "&month=" +month+ "&day=" + day;
}

function myNavFunction(id) {
    $("#date-popover").hide();
    var nav = $("#" + id).data("navigation");
    var to = $("#" + id).data("to");
    console.log('nav ' + nav + ' to: ' + to.month + '/' + to.year);
}

function nav(time, date, name, email, phone_number){
    window.location = "/reservations/book/?time=" +time +"&date=" + date + "&name=" + name +
        "&email=" + email + "&phone_number=" + phone_number
}

$(document).ready(function (){
        var time;
        var date;

        $('td').on('click', function(){
            time = $(this).attr('time');
            date = $(this).attr('date');
        });

         $('#save_appointment').on('click', function(){
            var name = document.getElementById("name").value;
            var email = document.getElementById("email").value;
            var phone_number = document.getElementById("phone_number").value;
            nav(time, date, name, email, phone_number)
        });

        function nav(time, date, name, email, phone_number){
            window.location = "/reservations/book/?time=" +time +"&date=" + date + "&name=" + name +
                                "&email=" + email + "&phone_number=" + phone_number
        }
    })