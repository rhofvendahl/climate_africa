$(document).ready(function() {
    console.log('hey');
    if (window.innerWidth <= 800 || window.innerHeight <= 800) {
        $('body').append($('#phone-screen > *'));
        $('#phone').hide();
    }
});
