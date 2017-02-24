/**
 * Created by Anders on 2/22/2017.
 */
(function app() {
        "use strict";

        function caesarCipher(encrypt) {
            if (typeof encrypt === 'undefined') {
                var encrypt = true;
            }


            var input = document.getElementById("userInput").value;
            var key = Number(document.getElementById("key").value);
            var alphabet = "abcdefghijklmnopqrstuvwxyz ".split("");
            var original_slice = alphabet.slice(key);
            var key_slice = alphabet.slice(0, key);
            var combined = original_slice.concat(key_slice);

            var codex = {};

            if (encrypt) {
                for (var i = 0; i < alphabet.length; i++) {
                    codex[alphabet[i]] = combined[i];
                }

            } else {
                for (var i = 0; i < alphabet.length; i++) {
                    codex[combined[i]] = alphabet[i];
                }
            }

            var encrypted_text = Array();
            for (var i = 0; i < input.length; i++) {
                var letter = input[i];
                encrypted_text.push(codex[letter]);
            }

            alert(encrypted_text.join(""));
        }


        var enc_button = document.getElementById("encrypt");
        enc_button.addEventListener("click", function (evt) {
            evt.preventDefault();
            caesarCipher(true);

        });

        var dec_button = document.getElementById("decrypt");
        dec_button.addEventListener("click", function (evt) {
            evt.preventDefault();
            caesarCipher(false);

        });


    })();