
let url = "https://data.calgary.ca/resource/rhkg-vwwp.json?status=Active&zone_type=Parking Zone&$$app_token=uyOXQ2JFvkleBIzNmLdEsrCQj";

    
    // Intialize our map
    var center = new google.maps.LatLng(41.7656874,-72.680087);
    var mapOptions = {
      zoom: 8,
      center: center
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
    
    // Retrieve our data and plot it
    $.getJSON(url, function(data, textstatus) {
          console.log(data);
          $.each(data, function(i, entry) {
              var marker = new google.maps.Marker({
                  position: new google.maps.LatLng(entry.location_1.latitude, 
                                                   entry.location_1.longitude),
                  map: map,
                  title: location.name
              });
          });
    });


