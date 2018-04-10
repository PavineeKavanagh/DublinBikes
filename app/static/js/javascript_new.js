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
            var marker = new google.maps.Marker({
                position: { lat: station.Latitude, lng: station.Longitude },
                map: map,
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
                            '</div ><div class=content-numbers>' + '<div class="column"><span id="contentHolder">Bikes:</span><span id="contentNum">' +
                            marker.availableBikes + '</span></div>' + '<div class="column"><span id="contentHolder">Stands:</span><span id="contentNum">' +
                            marker.availableStands + '</span></div>' + '</div>' + '<div id="content-lud"><span style="font-weight:bold">Last Update at:</span> ' + new Date(marker.lud) + '</div>' +
                            '</div >' + '</div>';
                        infowindow.setContent(contentString);
                        infowindow.open(map, marker);   
                }
            })(marker));
            function drawChart(marker) {
                var divElem = document.getElementById("weatherOver");
                divElem.style.display="block";
                var jqxhr = $.getJSON("/stations/" + marker.number, function (data) {
                    console.log(data.stationsId);
                    var newdata = data.stationsId;
                    var node = divElem;
                    chart = new google.visualization.ColumnChart(node);

                    var chart_data = new google.visualization.DataTable();
                    chart_data.addColumn('datetime','Time of Day');
                    chart_data.addColumn('number','Available Bikes');
                    _.forEach(newdata, function(row){
                        chart_data.addRow([new Date(row.time),row.availableBikes]);
                    });
                    var options = {
                        title: 'Available Bikes',
                        colors: ['#9575cd','#33ac71'],
                        hAxis: {
                            title: 'Time of Day',
                            format: "E HH:mm",
                            slantedText: true,
                            slantedTextAngle: 30,
                        },
                        vAxis: {
                            title: '#'
                        }
                    };
                    chart.draw(chart_data, options);
                });
            } google.charts.load('current', { 'packages': ['table', 'map', 'corechart'] });
            
        });
    })
    .fail(function () {
        console.log("error");
    })
     
})





