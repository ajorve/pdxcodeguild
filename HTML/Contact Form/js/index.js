// When the browser is ready...
  $(function() {
    // validate
    $("#encrypt").validate({
        // Set the validation rules
        rules: {
            name: "required",
            key: {
                required: true,
                key: true
            },
            message: "required"
        },
        // Specify the validation error messages
        messages: {
            // name: "Please enter your name",
            key: "Please enter a key",
            message: "Please enter a message tp encrypt"
        },
        // submit handler
        submitHandler: function(form) {
          //form.submit();
           $(".message").show();
           $(".message").fadeOut(10000);
        }
    });

    $("#decrypt").validate({
        // Set the validation rules
        rules: {
            name: "required",
            key: {
                required: true,
                key: true
            },
            message: "required"
        },
        // Specify the validation error messages
        messages: {
            // name: "Please enter your name",
            key: "Please enter a vaild key",
            message: "Please enter a message tp decrypt"
        },
        // submit handler
        submitHandler: function(form) {
          //form.submit();
           $(".message").show();
           $(".message").fadeOut(10000);
        }
    });
  });

