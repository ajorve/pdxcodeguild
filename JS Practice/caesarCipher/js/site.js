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
            key: "Please enter a valid email address",
            message: "Please enter a message"
        },
        // submit handler
        submitHandler: function(form) {
          //form.submit();
           $(".message").show();
           $(".message").fadeOut(45000);
        }
    });
  });