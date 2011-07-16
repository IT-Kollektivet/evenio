function toggle_login_form(object_clicked) {
  $("#login_form").toggle('fast');
  $(object_clicked).parent().toggleClass('selected');
}

$(function() {
  $( ".datePicker" ).datetimepicker({
      dateFormat: 'dd.mm.yy',
      timeFormat: 'hh:mm',
      timeText: 'Klokken',
      hourText: 'Time',
      minuteText: 'Minut',
      currentText: 'Nu',
      closeText: 'Luk'
  });
});
