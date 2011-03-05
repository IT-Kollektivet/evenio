/**
 * tutorial for async testing: http://net.tutsplus.com/tutorials/javascript-ajax/how-to-test-your-javascript-code-with-qunit/
 */
function successCallback(data, textStatus, jqXHR) {
  var status = data.status;
  ok(true, status);
}
function failedCallback(data, textStatus, jqXHR) {
  var status = data.status;
  ok(true, status);
}

module("List Events", {
  setup: function () {
    this.uriBase = "/evenio/";
    //this.uriBase = "http://192.168.1.102:8000/evenio/";
    $.ajaxSetup({
      async: true
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
  
  $.ajax(this.uriBase + '2011/05/', {
    success: successCallback,
    error: failedCallback
  });

  $.ajax(this.uriBase + '2011/05/01', {
    success: successCallback,
    error: failedCallback
  });
  
  setTimeout(function() {  
    start();  
  }, 5000);  
});