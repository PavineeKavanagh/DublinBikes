function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: { 'lat': 53.341833, 'lng': -6.231291 }
    });

    // Array to label each marker
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWX';
    
    // Adding some markers to the Map
    var markers = locations.map(function (location,i) {
        return new google.maps.Marker({
            position:location,
            label: labels[ i % labels.length]
        });        
    });

    // Adding a marker clusterer to manage the clustering
    var markerCluster = new MarkerClusterer(map, markers, { imagePath:'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

}