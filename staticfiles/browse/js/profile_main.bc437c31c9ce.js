$(document).ready(function() {
    // Would be good to turn all this junk into a simple "render" function, arguments for "supported", "n_supporters"
    var show_support_button = function() {
        $('#unsupport-button').hide() // red
        $('#support-button').show() // not red
    };

    var show_unsupport_button = function() {
        $('#support-button').hide() // not red
        $('#unsupport-button').show() // red
    };
    console.log(supported);

    if (supported) {
        show_unsupport_button();
    } else {
        show_support_button();
    }

    $('#support-button').click(function() {
        fetch(supportUrl, {method: 'post'})
        .then(
            response => response.json()
        ).then(data => {
            $('#supports').html(data.n_supporters)
            if (data.supported == 'true') {
                show_unsupport_button();
            } else {
                show_support_button();
            }
        });
    });

    $('#unsupport-button').click(function() {
        fetch(unsupportUrl, {method: 'post'}).then(
            response => response.json()
        ).then(data => {
            $('#supports').html(data.n_supporters)
            if (data.supported == 'true') {
                show_unsupport_button();
            } else {
                show_support_button();
            }
        });
    });
});
