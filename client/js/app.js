var backend = document.getElementById('backend');
var $list = document.getElementsByTagName('my-app')[0];
meta = document.querySelector('#meta');

var google = google || {};

var dataEvent; // The custom Event that will be created
 if (document.createEvent) {
   dataEvent = document.createEvent("HTMLEvents");
   dataEvent.initEvent("data-available", true, true);
 } else {
   dataEvent = document.createEventObject();
   dataEvent.eventType = "data-available";
 }
 dataEvent.eventName = "data-available";

var server;

var backend = document.getElementById('backend');
  backend.addEventListener('google-api-load', function(e) {
    server = backend.api;
    request = server.get_activities({
        lat: 34,
        lng: 34,
    });
    request.execute(function(resp) {
      meta.value = resp.activites;
      if (document.createEvent) {
        document.dispatchEvent(dataEvent);
      } else {
        document.fireEvent("on" + dataEvent.eventType, dataEvent);
      }
    });
});
