var speed;
$(document).ready(function(){
    $("#sensorf").mouseenter(function(){
        $("#sensorf").stop().animate({height:"260px"},500);
                             });
    $("#sensorf").mouseleave(function(){
        $("#sensorf").stop().animate({height:"60px"},500);
                            });
    $("#sensorg").mouseenter(function(){
        $("#sensorg").stop().animate({height:"260px"},500);
                            });
    $("#sensorg").mouseleave(function(){
        $("#sensorg").stop().animate({height:"60px"},500);
                            });
    $("#blockf").mouseover(function(e){
        speed = e.clientY-249;
        $("#status").html(speed);
        function a(){
            $("#slidef").style.top = $("#slidef").style.top - (50-speed)/5;
            setTimeout(a, 100);
                           }
/*function a(e){
        $("#status").html(e.clientX + " " + (e.clientY- 249));
                           setTimeout(a,100);*/
                           });
                  
})