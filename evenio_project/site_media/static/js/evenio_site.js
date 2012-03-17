function toggle_login_form(object_clicked) {
  $("#login_form").toggle('fast');
  $(object_clicked).parent().toggleClass('selected');
}

$(function() {
  $( ".datePicker" ).datetimepicker({
      dateFormat: 'dd/mm/yy',
      timeFormat: 'hh:mm',
      hour: 12,
      timeText: 'Klokken',
      hourText: 'Time',
      minuteText: 'Minut',
      currentText: 'Nu',
      closeText: 'Luk',
      showButtonPanel: false,
      showAnim: 'clip',
      showOtherMonths: true,
      selectOtherMonths: true,
      showWeek: true,

      beforeShow: function(input, inst){
        inst.dpDiv.css({marginTop: -input.offsetHeight + 'px', marginLeft: input.offsetWidth + 'px'});
      }
  });
});
