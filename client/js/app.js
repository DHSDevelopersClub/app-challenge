function loaded() {
  console.log('loadeded');
}

var server;

var backend = document.getElementById('backend');
  backend.addEventListener('google-api-load', function(event) {
    server = backend.api;
    request = server.get_activities({
        lat: 34,
        lng: 34,
    });
    request.execute(function(resp) {
      console.log('resp: ');
      console.log(resp.activites[1].user_created_disrcription);
    });
});
