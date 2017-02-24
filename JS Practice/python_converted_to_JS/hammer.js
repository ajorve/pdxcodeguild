/**
 * Created by Anders on 2/20/2017.
 */
"use strict";
(function app() {
        function meal(time) {
            var message;
            if ((time >= 22) && (time <= 4)) {
                message = "Hammer time."
            } else if ((time >= 7) && (time <= 9)) {
                message = "Breakfast time."
            } else if ((time >= 12 && time <= 14)) {
                message = "Lunch time."
            } else if ((time >= 19) && (time <= 21)) {
                message = "Dinner time."
            } else if (time >= 25) {
                message = "Not a valid time."
            } else if ((time <= 0) || (time >= 24)) {
                message = "No meal scheduled at this time."
            } else {
                message = "Hammer time."
            }

            alert(message)
        }

        var time = Number(prompt("What time is it? Please use whole number, no zeros(3, 4, 13, etc): "));
        meal(time);
    })();