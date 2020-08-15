$(document).ready(function() {
    if (window.innerWidth <= 800 || window.innerHeight <= 800) {
        $('body').append($('#phone-screen > *'));
        $('#phone').hide();
    }
    alert('width: ' + window.innerWidth + ', height: ' + window.innerHeight);
});
