// Get the map
function initMap() {
    var mapOptions = {
        zoom: 15,
        center: { 'lat': 53.346973, 'lng': -6.256796 },
    }                                                                       // ----- Get the optional values for the Map
    // Setting the map
    map = new google.maps.Map(document.getElementById("map"), mapOptions); // ------ Populate the map
    
}

$( document ).ready(function () {
    var jqxhr = $.getJSON("/stations", function (data) {
        var stations = data.stations;
        // console.log('stations', stations);
        // Plotting the markers
        var infowindow = new google.maps.InfoWindow();
        _.forEach(stations,function(station) {
            if (station.Status == 'OPEN') {
                var bikePercent = (station.availableBikes / station.TotalStands); // --------- Calculating the percentage of number of bikes in each stand
                if (bikePercent <= 0.25) {
                    // console.log("Less than 25%"+i);
                    // RED MARKER
                    iconbase = 'static/img/marker_red.png';
                    latLng = { lat: station.Latitude, lng: station.Longitude };
                    titleVal = station.StationName;
                } else if ((bikePercent > 0.25) && (bikePercent < 0.75)) {
                    // console.log("Greater than 25%"+i);
                    // ORANGE MARKER
                    iconbase = 'static/img/marker_orange.png';
                    latLng = { lat: station.Latitude, lng: station.Longitude };
                    titleVal = station.StationName;
                } else {
                    // console.log("Greater than 75%"+i);
                    // GREEN MARKER
                    iconbase = 'static/img/marker_green.png';
                    latLng = { lat: station.Latitude, lng: station.Longitude };
                    titleVal = station.StationName;
                }
            } else {
                iconbase = 'static/img/marker_gray.png';
                latLng = { lat: station.Latitude, lng: station.Longitude };
                titleVal = station.StationName;
            }
            var marker = new google.maps.Marker({
                position: latLng,
                icon: iconbase,
                map: map,
                title: titleVal
            });
            var contentString;
            if ((station.Status == 'OPEN') && (station.availableBikes > 0)) {
                contentString = '<div id="content">' +
                    '<div id = "content-station" >' + station.StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                    station.availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                    station.availableStands + '</span></div>' + '</div id="bookButton"><buttontype="button" class="btn btn-primary" style="margin-top:0px">Get a Bike</button></div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + station.LUD + '</div>' +
                    '</div >' + '</div>';
            } else if ((station.Status == 'OPEN') && (station.availableBikes == 0)) {
                contentString = '<div id="content">' +
                    '<div id = "content-station" >' + station.StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                    station.availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                    station.availableStands + '</span></div>' + '</div id="bookButton"><buttontype="button" class="btn btn-secondary disabled" style="margin-top:0px" aria-disabled="true">Get a Bike</button></div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + station.LUD + '</div>' +
                    '</div >' + '</div>';
            } else {
                contentString = '<div id="content">' +
                    '<div id = "content-station" >' + station.StationName +
                    '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Station Closed</span></div>' +
                    '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + station.LUD + '</div>' +
                    '</div >' + '</div>';
            }
            google.maps.event.addListener(marker, 'click', (function (marker) {
                return function () {    
                    drawChart(this, contentString, station.StationNum);
                    infowindow.setContent(contentString);
                    infowindow.open(map, marker);   
                }
            })(marker));
            
        });
    })
    .fail(function () {
        console.log("error");
    })
    
})

function drawChart(marker, contentString, station_id) {
    var jqxhr = $.getJSON("/stations/" + station_id, function (data) {
        console.log(data.stationsId);
    });


}



