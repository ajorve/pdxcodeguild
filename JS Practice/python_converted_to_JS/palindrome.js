/**
 * Created by Anders on 2/21/2017.
 */

(function app() {
    "use strict";

    function palindrome(word) {

        var re = /[^A-Za-z0-9]/g;
        word = word.toLowerCase().replace(re, '');
        var len = word.length;
        for (var i = 0; i < len / 2; i++) {
            if (word[i] !== word[len - 1 - i]) {
                alert('False');
            }
        }
        alert('True');

    }

    var word = prompt("What word or number would you like to check if palindrome? >> ");
    palindrome(word);
})();