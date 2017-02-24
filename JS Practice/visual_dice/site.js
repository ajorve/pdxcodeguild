(function app() {
    "use strict";

    function create_dice() {
        var $user_input = $('#user_input');
        var $new_dice = $('<item>');
        $new_dice.css({'background-image': 'url(img/dice_rolling.gif)'});

        $('#dice_table').append($new_dice);

    }

    function rollDice() {
        var $dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'];
        var $status = $("status");
        var $d1 = Math.floor(Math.random() * 6) + 1;
        var $d2 = Math.floor(Math.random() * 6) + 1;
        var $diceTotal = $d1 + $d2;
        $d1 = $('#die1');
        $d2 = $('#die2');
        $status("You rolled " + $diceTotal + ".");
        if ($d1 == $d2) {
            $status += " DOUBLES! You get a free turn!!";
        }
    }

    var $roll_button = $('#submit');
    $roll_button.on('click', function (event) {
        event.preventDefault();
        //above prevents page from refreshing
        create_dice();
        //above actually runs the to do program
        $('#user_input').val("");
        //clears the input field
    };


})();

