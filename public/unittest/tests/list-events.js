function successCallback(data, textStatus, jqXHR) {
  ok(true);
}
function failedCallback(data, textStatus, jqXHR) {
  ok(true, textStatus);
}

module("List Events", {
  setup: function () {
//    this.uriBase = "http://192.168.1.102:8000/evenio/list";
    $.ajaxSetup({
      async: true,

    });
  },
  teardown: function () {

  }
});
/* Test#1 */
test('Testing event lists', 3, function () {
  stop();
  $.ajax(this.uriBase, {
    success: successCallback,
    error: failedCallback
  });
  
  $.ajax(this.uriBase + '/2011/05', {
    success: successCallback,
    error: failedCallback
  });

  $.ajax(this.uriBase + '/2011/05/01', {
    success: successCallback,
    error: failedCallback
  });
  
  setTimeout(function() {  
    start();  
  }, 2000);  
});