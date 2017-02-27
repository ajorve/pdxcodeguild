(function app(){
    "use strict";

    function add_person(person){
        var $name = person['name']['first'] + " " + person['name']['last'];
        var $dob = person['dob'];
        var $cell = person['cell'];
        var $email = person['email'];
        var $location = person['location']['city'];
        var $picture = person['picture']['thumbnail'];

        var $person_container = $('<div class="user_box">');

        var $p_name = $('<p id="name">').text($name);
        var $p_dob =$('<p id="dob">').text($dob);
        var $p_cell =$('<p id="cell">').text($cell);
        var $p_email =$('<p id="email">').text($email);
        var $p_location =$('<p id="location">').text($location);
        var $p_picture =$('<img id="picture">').attr('src', $picture);

        $($person_container).append($p_name, $p_dob, $p_cell, $p_email, $p_location, $p_picture);
        $('.container').append($person_container);
    }

    function get_data(qty) {
        $.ajax({
         url: 'https://api.randomuser.me',   // Target Server
         method: 'GET',                      // Request Verb
         data: {'results': qty},             // Request Params
         success: function(rsp){             // Success Handler
            var people = rsp['results'];
            $.each(people, function (index, person) {
                add_person(person);
            })

            },
         error: function(err){               // Error Handler
            console.log(err);
            }
         });
    }

    get_data(2);

})();