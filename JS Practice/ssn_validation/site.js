/**
 * Created by Anders on 2/22/2017.
 */
(function ssnValidation() {
    document.getElementById("submit").addEventListener("click", function () {
        var pattern = /\d{3}-?\d{2}-?\d{4}/;
        var ssn = document.getElementById("ssn").value;
        var res = pattern.test(ssn.value);
        alert("LLAMAS");
        if (!res) {
            ssn.match(/\d*/g).join('');
            ssn.match(/(\d{0,3})(\d{0,2})(\d{0,4})/).slice(1).join('-');
            ssn.replace(/-*$/g, '');
        }
    });
})();
