/*function test1()
{
    a = document.getElementById("navimess");
    a.style.top = "0px";
}
function test2()
{
    a = document.getElementById("navimess");
    a.style.top = "-90px";
*/
$(document).ready(function(){
                  $("#sensor").mouseenter(function(){
                                       //document.getElementById("back").style.z-index = 10;
                                          $("#navimess").stop().animate({top:"100px", opacity:"1"},900);
                                          $("#navifile").stop().animate({top:"160px", opacity:"1"},700);
                                          $("#navistat").stop().animate({top:"220px", opacity:"1"},500);
                                          $("#sensor").stop().animate({height:"270px"},500);
                                        });
                  $("#sensor").mouseleave(function(){
                                          $("#navimess").stop().animate({top:"0px", opacity:"0.3"},300);
                                          $("#navifile").stop().animate({top:"0px", opacity:"0.3"},600);
                                          $("#navistat").stop().animate({top:"0px", opacity:"0.3"},900);
                                          $("#sensor").stop().animate({height:"90px"},900);
                                        });
                  })