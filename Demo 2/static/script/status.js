$(document).ready(function(){
    cur_i = $("#slidef").height() / 30;
    anchor = 0;
    cur_y = 0;
    cur_b = 0;
    active = 0;
    $("#sensorf").mouseenter(function(){
        $("#sensorf").stop().animate({height:"272px"},500);
    });
    $("#sensorf").mouseleave(function(){
        $("#sensorf").stop().animate({height:"60px"},500);
    });
    $("#sensorg").mouseenter(function(){
        $("#sensorg").stop().animate({height:"272px"},500);
    });
    $("#sensorg").mouseleave(function(){
        $("#sensorg").stop().animate({height:"60px"},500);
    });
    function a(){
        if(active == 1){
        $("#naruhodo").html(cur_y + "cur_b=" + cur_b + "\n anchor ="+anchor);
        if(cur_b == 0)
        {
            if((cur_y <= 70) && (anchor != 0))
            {
                cur_b = 1;
                time = (cur_y + 30) * 5;
                $("#slidef").animate(
                {
                    top : (-(anchor-1)*30).toString() + "px"
                },
                time,
                "linear",
                function()
                {
                    anchor --;
                    cur_b = 0;
                })
            }
            if((cur_y>=142) && (anchor != cur_i - 7))
            {
                cur_b = 1;
                time = (242 - cur_y) * 5;
                $("#slidef").animate({
                    top : (-(anchor + 1) * 30).toString() + "px"
                },
                time,
                "linear",
                function() 
                {
                    anchor ++;
                    cur_b = 0;
                })
            }
        }
        }
        setTimeout(a, 30);
    }
    a();
    $("#blockf").mouseenter(function()
    {
        active = 1;
        })
    $("#blockf").mouseover(function(e){
        cur_y = e.clientY - 247;
    })
    $(".fri").mouseenter(function()
    {
        $(this).css("background-color", "#cf3a00");
        $("#blockf").css("overflow", "hidden");
    })
        $(".fri").mouseleave(function(){
        $(this).css("background-color", "#df4a10");
    })
    $("#blockf").mouseleave(function(){
        $("#slidef").animate({
            top : (-anchor * 30).toString() + "px"
            },5000,"swing",function(){cur_b=0, active=0});
        cur_b=0;
    })
})
