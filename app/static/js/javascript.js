// Get the map
function initMap() {
    var mapOptions = {
        zoom: 15,
        center: {
            'lat': 53.346973,
            'lng': -6.256796
        },
    } // ----- Get the optional values for the Map
    // Setting the map
    map = new google.maps.Map(document.getElementById("map"), mapOptions); // ------ Populate the map

}

$(document).ready(function () {

    var jqxhr = $.getJSON("/stations", function (data) {
            var stations = data.stations;
            // console.log('stations', stations);
            // Plotting the markers
            var infowindow = new google.maps.InfoWindow();
            var divElem = document.getElementById("weatherOver");
            _.forEach(stations, function (station) {
                if (station.Status == 'OPEN') {
                    var bikePercent = (station.availableBikes / station.TotalStands); // --------- Calculating the percentage of number of bikes in each stand
                    // console.log(bikePercent+' '+i);
                    if (bikePercent <= 0.25) {
                        // console.log("Less than 25%"+i);
                        // RED MARKER
                        iconbase = 'static/img/pin_red.png';
                        latLng = {
                            lat: station.Latitude,
                            lng: station.Longitude
                        };
                        titleVal = station.StationName;
                    } else if ((bikePercent > 0.25) && (bikePercent < 0.75)) {
                        // console.log("Greater than 25%"+i);
                        // ORANGE MARKER
                        iconbase = 'static/img/pin_orange.png';
                        latLng = {
                            lat: station.Latitude,
                            lng: station.Longitude
                        };
                        titleVal = station.StationName;
                    } else {
                        // console.log("Greater than 75%"+i);
                        // GREEN MARKER
                        iconbase = 'static/img/pin_green.png';
                        latLng = {
                            lat: station.Latitude,
                            lng: station.Longitude
                        };
                        titleVal = station.StationName;
                    }
                } else {
                    iconbase = 'static/img/pin_gray.png';
                    latLng = {
                        lat: station.Latitude,
                        lng: station.Longitude
                    };
                    titleVal = station.StationName;
                }
                var marker = new google.maps.Marker({
                    position: {
                        lat: station.Latitude,
                        lng: station.Longitude
                    },
                    map: map,
                    icon: iconbase,
                    title: station.StationName,
                    number: station.StationNum,
                    status: station.Status,
                    availableBikes: station.availableBikes,
                    availableStands: station.availableStands,
                    lud: station.LUD
                });
                google.maps.event.addListener(marker, 'click', (function (marker) {
                    return function () {
                        drawChart(marker);
                        var availability = station.availability;
                        var lud = station.lud;
                        var contentString = '<div id="content">' +
                            '<div id = "content-station" >' + marker.title +
                            '<div>Status: ' + marker.status + '</div></div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                            marker.availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                            marker.availableStands + '</span></div>' + '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + (marker.lud) + '</div>' +
                            '</div >' + '</div>';
                        infowindow.setContent(contentString);
                        infowindow.open(map, marker);
                    }
                })(marker));

                function drawChart(marker) {
                    divElem.style.display = "block";
                    var jqxhr = $.getJSON("/stations/" + marker.number, function (data) {
                        console.log(data.stationsId);
                        var newdata = data.stationsId;
                        var node = divElem;
                        chart = new google.visualization.ColumnChart(node);

                        var chart_data = new google.visualization.DataTable();
                        chart_data.addColumn('datetime', 'Time of Day');
                        chart_data.addColumn('number', 'Available Bikes');
                        _.forEach(newdata, function (row) {
                            chart_data.addRow([new Date(row.time), row.availableBikes]);
                        });
                        var options = {
                            title: 'Popularity Chart',
                            colors: ['#9575cd', '#33ac71'],
                            hAxis: {
                                title: 'Time of Day',
                                format: "HH:mm",
                                slantedText: true,
                                slantedTextAngle: 30,
                            },
                            vAxis: {
                                title: 'Average Number of Bikes'
                            }

                            
                        };
                        chart.draw(chart_data, options);
                    });
                }
                google.charts.load('current', {
                    'packages': ['table', 'map', 'corechart']
                });

            });
            google.maps.event.addListener(infowindow, 'closeclick', function () {
                divElem.style.display = "none";
                // then, remove the infowindows name from the array
            });
        })
        .fail(function () {
            console.log("error");
        })

})

