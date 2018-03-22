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
    var infowindows = [];
    var infowindowcontent = [];
    for (var i = 0; i < locations.length; i++) {
        var contentString = '<div id="content">' +
            '<div id = "content-station" >' + locations[i].name +
            '</div ><div class=content-numbers>'+
            '<div class="column"> Bikes' + locations[i].availBikes +
            '</div>' + '<div class="column">' + locations[i].availStands +
            '</div>' + '</div>' + '<div id="content-lud">LUD</div>' +
            '</div >' + '</div>';
        infowindowcontent.push(contentString);
    }

    var infowindow = new google.maps.InfoWindow();
    for (var i = 0; i < locations.length; i++) {
        var bikePercent = (locations[i].availBikes / locations[i].tStands) * 100; // --------- Calculating the percentage of number of bikes in each stand
        var iconbase = '';
        var latLng = {};
        titleVal = '';
        if (bikePercent <= 0.25){
            // console.log("Less than 25%"+i);
            // RED MARKER
            iconbase = 'static/img/marker_red.png';
            latLng = { lat: locations[i].lat, lng: locations[i].lng};
            titleVal = locations[i].name;
        } else if (bikePercent > 0.25 && bikePercent < 0.75){
            // console.log("Greater than 25%"+i);
            // ORANGE MARKER
            iconbase = 'static/img/marker_orange.png';
            latLng = { lat: locations[i].lat, lng: locations[i].lng };
            titleVal = locations[i].name;
        } else {
            // console.log("Greater than 75%"+i);
            // GREEN MARKER
            iconbase = 'static/img/marker_green.png';
            latLng = { lat: locations[i].lat, lng: locations[i].lng };
            titleVal = locations[i].name;
        }
        var marker = new google.maps.Marker({
            position: latLng,
            icon: iconbase,
            title: titleVal
        });  
        markers.push(marker);
        // The below code is referred from stack overflow
        google.maps.event.addListener(marker,'click',(function(marker,i){
            return function() {
                infowindow.setContent(infowindowcontent[i]);
                infowindow.open(map,marker);
            }
            })(marker, i));
        }
    var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}