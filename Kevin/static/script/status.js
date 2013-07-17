$(document).ready(function(){
                  $("#sensorf").mouseenter(function(){
                                          //$("#navimess").stop().animate({top:"100px", opacity:"1"},900);
                                          //$("#navifile").stop().animate({top:"160px", opacity:"1"},700);
                                          //$("#navistat").stop().animate({top:"220px", opacity:"1"},500);
                                           $("#sensorf").stop().animate({height:"270px"},500);
                                           $("#groups").stop().animate({top:"100px"},500)
                                           });
                  $("#sensorf").mouseleave(function(){
                                          $("#navimess").stop().animate({top:"0px", opacity:"0.3"},300);
                                          $("#navifile").stop().animate({top:"0px", opacity:"0.3"},600);
                                          $("#navistat").stop().animate({top:"0px", opacity:"0.3"},900);
                                          $("#sensor").stop().animate({height:"90px"},900);
                                          });
                  })