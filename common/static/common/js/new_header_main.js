$(document).ready(function() {
    var animating = false;

    var hideHeader = function() {
        if (!animating) {
            animating = true;
            // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
            $('.container-fluid > div:first-child').animate({top: '0'}, 400, function() {
                $('#header').hide();
                animating = false;
            });
            $('#return-header').fadeIn(400);
        }
    }

    $('.container-fluid > div:first-child').css({top: '6rem'});
    var showHeader = function() {
        if (!animating) {
            $('#header').show();
            animating = true;
            // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
            $('.container-fluid > div:first-child').animate({top: '6rem'}, 400, function() {
                animating = false;
            });
            $('#return-header').fadeOut(400);

            if (hideHeaderTimeout) {
                clearTimeout(hideHeaderTimeout);
                hideHeaderTimeout = null;
                hideHeaderTimeout = setTimeout(hideHeader, 4000);
            }
        }
    }

    hideHeaderTimeout = setTimeout(hideHeader, 5000);

    // Firefox
    $('html').on('DOMMouseScroll', function(event) {
        var delta = event.originalEvent.detail;

        if (delta > 0) {
            showHeader();
        } else {
            hideHeader(0);
        }
    });

    // Chrome, IE, Opera, Safari (& hopefully others)
    $('html').on('mousewheel', function(event) {
        var delta = event.originalEvent.wheelDelta;

        if (delta > 0) {
            showHeader();
        } else {
            hideHeader();
        }
    });

    $('#return-header').click(function() {
        showHeader();
    });
});
