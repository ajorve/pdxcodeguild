/**
 * Created by Anders on 2/22/2017.
 */

(function app() {
    "use strict";

    function todo() {
        var $input = $('#input');
        var $form = $('#form');
        var $new_item = $('<li>');

        var $button = $('<span>x</span>');
        $button.on('click', function (evt) {
            $new_item.toggle()

        });

        var $content = $input.text('<span>');
        $content.append($input.val(""));
        $new_item.append($button);
        $new_item.append($content);
        $form.append($new_item);
    }

    var $submit = $('#submit');
    $submit.on('click', function (evt) {
        event.preventDefault();
        todo();
    })
})();