  var urlstr = location.href;
  //alert((urlstr + '/').indexOf($(this).attr('href')));
  var urlstatus=false;
  $("#menu_list a").each(function () {
    if ((urlstr + '/').indexOf($(this).attr('href')) > -1&&$(this).attr('href')!='') {
      $(this).addClass('cur'); urlstatus = true;
    } else {
      $(this).removeClass('current');
    }
  });
  if (!urlstatus) {$("#menu_list a").eq(0).addClass('current'); }