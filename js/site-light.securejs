$(document).ready(function(){
  $('.open-lbox').click(function(e){
    e.preventDefault();
    openLbox($(this).data('lboxid'));
  });
});

function openLbox(lboxid) {
  $(lboxid).show().siblings().hide();
  $('.lboxed').lightbox_me({
    centered: true,
    closeClick: false
  });
}