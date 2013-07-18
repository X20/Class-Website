$(document).ready(function(){
                  cur_i = $("#slidef").height() / 30;
                  anchor = 0;
                  cur_y = 0;
                  cur_b = 0;
                  active = 0;
                  $("#sensorf").mouseenter(function(){
                                           var ht = 272;
                                           if (Number($("#slidef").height()) + 60 < 272) ht = Number($("#slidef").height()) + 60;
                                           var time = 2.5 * (ht - 60);
                                           $("#sensorf").stop().animate({ height: ht.toString()+"px" }, time);
                                           });
                  $("#sensorf").mouseleave(function () {
                                           $("#sensorf").stop().animate({ height: "60px" }, 500);
                                           });
                  $("#sensorg").mouseenter(function () {
                                           var ht = 272;
                                           if (Number($("#slideg").height() + 60) < 272) ht = Number($("#slideg").height()) + 60;
                                           var time = 2.5 * (ht - 60);
                                           $("#sensorg").stop().animate({ height: ht.toString() + "px" }, time);
                                           });
                  $("#sensorg").mouseleave(function () {
                                           $("#sensorg").stop().animate({ height: "60px" }, 500);
                                           });
                  /*$("#blockf").mouseover(function (e) {
                                         speed = e.clientY - 249;
                                         $("#status").html(speed);
                                         function a(){
                                         $("#slidef").style.top = $("#slidef").style.top - (50 - speed) / 5;
                                         setTimeout(a, 100);
                                         }
                                         });*/
                  function a(){
                  if(active == 1){
                  cur_i = $("#slidef").height() / 30;
                  $("#naruhodo").html(cur_y + "cur_b=" + cur_b + "\n anchor ="+anchor);
                  /*if(anchor < 0 || anchor >= cur_i)
                   {
                   $("#slidef").stop().animate(
                   top : "0px"
                   ),
                   50,
                   "linear",
                   function()
                   {
                   anchor = 0;
                   cur_b = 0;
                   }
                   }*/
                  if(cur_b == 0)
                  {
                  if((cur_y <= 66) && (anchor != 0))
                  {
                  cur_b = 1;
                  time = (cur_y + 20) * 5;
                  $("#slidef").stop().animate(
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
                  if((cur_y>=Number($("#blockf").height())- 66) && (anchor != cur_i - 7))
                  {
                  cur_b = 1;
                  time = (232 - cur_y) * 5;
                  $("#slidef").stop().animate({
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
                                         cur_y = e.clientY - $("#blockf").offset().top;
                                         })
                  $("#blockf").mouseleave(function(e){
                                          active = 0;
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
                                          $("#slidef").stop().animate({
                                                                      top : (-anchor * 30).toString() + "px"
                                                                      },500,"swing",function(){cur_b=0, active=0});
                                          cur_b=0;
                                          })
                  });