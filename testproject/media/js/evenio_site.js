function toggle_login_form(object_clicked) {
  $("#login_form").toggle('fast');
  $(object_clicked).parent().toggleClass('selected');
}

$(function() {
  $( ".datePicker" ).datetimepicker({
      dateFormat: 'dd.mm.yy',
      timeFormat: 'hh:mm',
      hour: 12,
      timeText: 'Klokken',
      hourText: 'Time',
      minuteText: 'Minut',
      currentText: 'Nu',
      closeText: 'Luk',
      showButtonPanel: false,
      showAnim: 'drop',
      showOtherMonths: true,
      selectOtherMonths: true,
      showWeek: true
  });
});
