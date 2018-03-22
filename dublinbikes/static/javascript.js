function initMap() {
    var mapOptions = {
        zoom: 15,
        center: { 'lat': 53.341833, 'lng': -6.231291 }
    }

    // Setting the map
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    // Changing the icons for the markers
    //Marker for each one
    var markers = [];
    for (var i = 0; i < locations.length; i++) {
        var bikePercent = (locations[i].availBikes / locations[i].tStands) * 100; // --------- Calculating the percentage of number of bikes in each stand
        if (bikePercent <= 0.25){
            // console.log("Less than 25%"+i);
            // RED MARKER
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
                icon: 'static/img/marker_red.png',
                map: map,
                title:locations[i].name
            });   
            // markers.push(marker);
        } else if (bikePercent > 0.25 && bikePercent < 0.75){
            // console.log("Greater than 25%"+i);
            // ORANGE MARKER
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
                icon: 'static/img/marker_orange.png',
                map: map,
                title:locations[i].name
            });   
            // markers.push(marker);
        } else {
            // console.log("Greater than 75%"+i);
            // GREEN MARKER
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
                icon: 'static/img/marker_green.png',
                map: map,
                title:locations[i].name
            });   
            // markers.push(marker);
        }
             
    }
}