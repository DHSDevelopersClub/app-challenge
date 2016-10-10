var backend = document.getElementById('backend');
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

backend.addEventListener('google-api-load', function(e) {
  getActivities(34, 34, backend.api);
});


function getActivities(latitude, longitude, server) {
  request = server.get_activities({
      lat: latitude,
      lng: longitude,
  });
  request.execute(function(resp) {
    meta.value = resp.activites;
    if (document.createEvent) {
      document.dispatchEvent(dataEvent);
    } else {
      document.fireEvent("on" + dataEvent.eventType, dataEvent);
    }
  });
}
