$(document).ready(function () {
    if (window.location.href.indexOf("maps") > -1) {
        alert("your url contains the name maps");
    }
});
function initMap() {
    var flag;
    if (window.location.href.indexOf("maps") > -1) {
        flag = "true";
    }
    var mapOptions = {
        zoom: 15,
        center: { 'lat': 53.346973, 'lng': -6.256796 },
        // styles: [
        //     { elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
        //     { elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
        //     { elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
        //     {
        //         featureType: 'administrative.locality',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#d59563' }]
        //     },
        //     {
        //         featureType: 'poi',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#d59563' }]
        //     },
        //     {
        //         featureType: 'poi.park',
        //         elementType: 'geometry',
        //         stylers: [{ color: '#263c3f' }]
        //     },
        //     {
        //         featureType: 'poi.park',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#6b9a76' }]
        //     },
        //     {
        //         featureType: 'road',
        //         elementType: 'geometry',
        //         stylers: [{ color: '#38414e' }]
        //     },
        //     {
        //         featureType: 'road',
        //         elementType: 'geometry.stroke',
        //         stylers: [{ color: '#212a37' }]
        //     },
        //     {
        //         featureType: 'road',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#9ca5b3' }]
        //     },
        //     {
        //         featureType: 'road.highway',
        //         elementType: 'geometry',
        //         stylers: [{ color: '#746855' }]
        //     },
        //     {
        //         featureType: 'road.highway',
        //         elementType: 'geometry.stroke',
        //         stylers: [{ color: '#1f2835' }]
        //     },
        //     {
        //         featureType: 'road.highway',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#f3d19c' }]
        //     },
        //     {
        //         featureType: 'transit',
        //         elementType: 'geometry',
        //         stylers: [{ color: '#2f3948' }]
        //     },
        //     {
        //         featureType: 'transit.station',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#d59563' }]
        //     },
        //     {
        //         featureType: 'water',
        //         elementType: 'geometry',
        //         stylers: [{ color: '#17263c' }]
        //     },
        //     {
        //         featureType: 'water',
        //         elementType: 'labels.text.fill',
        //         stylers: [{ color: '#515c6d' }]
        //     },
        //     {
        //         featureType: 'water',
        //         elementType: 'labels.text.stroke',
        //         stylers: [{ color: '#17263c' }]
        //     }
        // ]
    }

    // Setting the map
    map = new google.maps.Map(document.getElementById("map"), mapOptions);
    // Changing the icons for the markers
    //Marker for each one
    var markers = [];
    var infowindows = [];
    var infowindowcontent = [];
    for (var i = 0; i < locations.length; i++) {
        if (flag=="true"){
            if ((locations[i].Status == 'OPEN') && (locations[i].availableBikes>0)) {
                var contentString = '<div id="content">' +
                    '<div id = "content-station" >' + locations[i].StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                    locations[i].availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                    locations[i].availableStands + '</span></div>' + '</div id="bookButton"><buttontype="button" class="btn btn-primary" style="margin-top:0px">Get a Bike</button></div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + locations[i].LUD + '</div>' +
                    '</div >' + '</div>';
            } else if ((locations[i].Status == 'OPEN') && (locations[i].availableBikes == 0)){
                var contentString = '<div id="content">' +
                    '<div id = "content-station" >' + locations[i].StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                    locations[i].availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                    locations[i].availableStands + '</span></div>' + '</div id="bookButton"><buttontype="button" class="btn btn-secondary disabled" style="margin-top:0px" aria-disabled="true">Get a Bike</button></div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + locations[i].LUD + '</div>' +
                    '</div >' + '</div>';
            } else {
                var contentString = '<div id="content">' +
                    '<div id = "content-station" >' + locations[i].StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Station Closed</span></div>' +
                    '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + locations[i].LUD + '</div>' +
                    '</div >' + '</div>';
            }
        } else {
            if (locations[i].Status == 'OPEN') {
                var contentString = '<div id="content">' +
                    '<div id = "content-station" >' + locations[i].StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                    locations[i].availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                    locations[i].availableStands + '</span></div>' + '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + locations[i].LUD + '</div>' +
                    '</div >' + '</div>';
            } else {
                var contentString = '<div id="content">' +
                    '<div id = "content-station" >' + locations[i].StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Station Closed</span></div>' +
                    '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + locations[i].LUD + '</div>' +
                    '</div >' + '</div>';
            }
        }
        infowindowcontent.push(contentString);
    }

    var iconbase = '';
    var latLng = {};
    titleVal = '';
    var infowindow = new google.maps.InfoWindow();
    for (var i = 0; i < locations.length; i++) {
        if (locations[i].Status == 'OPEN') {
            var bikePercent = (locations[i].availableBikes / locations[i].TotalStands); // --------- Calculating the percentage of number of bikes in each stand
            // console.log(bikePercent+' '+i);
            if (bikePercent <= 0.25) {
                // console.log("Less than 25%"+i);
                // RED MARKER
                iconbase = 'static/img/marker_red.png';
                latLng = { lat: locations[i].Latitude, lng: locations[i].Longitude };
                titleVal = locations[i].StationName;
            } else if ((bikePercent > 0.25) && (bikePercent < 0.75)) {
                // console.log("Greater than 25%"+i);
                // ORANGE MARKER
                iconbase = 'static/img/marker_orange.png';
                latLng = { lat: locations[i].Latitude, lng: locations[i].Longitude };
                titleVal = locations[i].StationName;
            } else {
                // console.log("Greater than 75%"+i);
                // GREEN MARKER
                iconbase = 'static/img/marker_green.png';
                latLng = { lat: locations[i].Latitude, lng: locations[i].Longitude };
                titleVal = locations[i].StationName;
            }
        } else {
            iconbase = 'static/img/marker_gray.png';
            latLng = { lat: locations[i].Latitude, lng: locations[i].Longitude };
            titleVal = locations[i].StationName;
        }
        var marker = new google.maps.Marker({
            position: latLng,
            icon: iconbase,
            map: map,
            title: titleVal
        });
        // markers.push(marker);
        // The below code is referred from stack overflow
        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(infowindowcontent[i]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }
    // var markerCluster = new MarkerClusterer(map, markers,
    //     { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}