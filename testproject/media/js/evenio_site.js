function toggle_login_form(object_clicked) {
  $("#login_form").toggle('fast');
  $(object_clicked).parent().toggleClass('selected');
}

$(function() {
  $( ".datePicker" ).datepicker();
});
