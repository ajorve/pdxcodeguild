(function app() {
    "use strict";

    var markers = [];

    (function get_loc() {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            searchRadius(user_loc);
        });
    })();

    function searchRadius(user_loc) {
        var $submit = $('#submit');
        $submit.on('click', function (event) {
            event.preventDefault();
            var $meters = $('#input_meters').val();
            get_data(user_loc, $meters);
        })
    }

    function add_stop(stops) {
        var marker;
        $.each(stops, function (index, stop) {
            var stop_location = {lat: stop.lat, lng: stop.lng};
            var image = 'trimet.png';
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(stop_location.lat, stop_location.lng),
                animation: google.maps.Animation.DROP,
                icon: image,
                title: 'Bus Stop',
                map: map
            });
            markers.push(marker);
        })
    }

    function get_data(user_loc, meters) {
        $.ajax({
            url: 'https://developer.trimet.org/ws/V1/stops?data',   // Target Server
            method: 'GET',                                            // Request Verb
            data: {
                appID: '5900B924C08929BDA431DAA1B',
                ll: user_loc.lat + ", " + user_loc.lng,
                json: 'true',
                meters: meters
            },                                                       // Request Params
            success: function (rsp) {                                // Success Handler
                var bus_stops = rsp.resultSet.location;
                add_stop(bus_stops);
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }

    // Captures User Geolocation
})();