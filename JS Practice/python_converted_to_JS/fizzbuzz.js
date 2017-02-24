/**
 * Created by Anders on 2/21/2017.
 */

(function app() {
    "use strict";

    function fizz_buzz(stop_num) {

        var number_list = Array();

        for (var i = 1; i <= stop_num; i++) {
            if ((i % 3 === 0) && (i % 5 === 0)) {
                number_list.push("FizzBuzz");
            } else if (i % 3 === 0) {
                number_list.push("Fizz");
            } else if (i % 5 === 0) {
                number_list.push("Buzz");
            } else {
                number_list.push(i);
            }
        }
        return number_list;

    }

    function joined_buzz(number) {
        var number_list = fizz_buzz(number);
        return number_list.join(" ");
    }

    var stop_num = prompt("How many numbers would you like to FizzBuzz? >> ");
    var joined = joined_buzz(stop_num);
    document.write(joined);

})();