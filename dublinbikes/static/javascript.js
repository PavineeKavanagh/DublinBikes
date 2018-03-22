function initMap() {
    var mapOptions = {
        zoom: 12,
        center: { 'lat': 53.341833, 'lng': -6.231291 }
    }

    // Setting the map
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    //Marker for each one
    console.log(locations[0].lat)
    for (var i = 0; i < locations.length; i++) {
        var marker = new google.maps.Marker({
            position : new google.maps.LatLng(locations[i].lat,locations[i].lng),
            map : map
        });        
    }
}