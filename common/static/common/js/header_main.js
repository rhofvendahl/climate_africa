$(document).ready(function() {
    var animating = false;

    var hideHeader = function() {
        if (!animating) {
            animating = true;
            // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
            $('#header').animate({top: '-6rem'}, 400, function() {
                $('#header').hide();
                animating = false;
            });
            $('.container-fluid > div:first-child').animate({top: '0'}, 400);
            $('#return-header').fadeIn(400);
            // $('#return-header').animate({marginTop: ".7rem"}, 400);
            // headerHidden = true;
        }
    }

    $('.container-fluid > div:first-child').css({top: '6rem'});
    var showHeader = function() {
        if (!animating) {
            $('#header').show();
            animating = true;
            // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
            $('#header').animate({top: '0'}, 400, function() {
                animating = false;
            });
            $('.container-fluid > div:first-child').animate({top: '6rem'}, 400);
            $('#return-header').fadeOut(400);

            // $('#return-header').animate({marginTop: "-2.5rem"}, 400, function() {
            //     $('#return-header').hide();
            // });
            // headerHidden = false;

            // setTimeout(hideHeader, 4000);
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
            // console.log('scrollup', headerHidden);
            showHeader();
        } else {
            // console.log('scrolldown', headerHidden);
            hideHeader(0);
        }
    });

    // Chrome, IE, Opera, Safari (& hopefully others)
    $('html').on('mousewheel', function(event) {
        var delta = event.originalEvent.wheelDelta;

        if (delta > 0) {
            // console.log('scrollup')
            showHeader();
            // console.log('about to clear', hideHeaderTimeout)
            // console.log('cleared', hideHeaderTimeout)
        } else {
            // console.log('scrolldown')
            hideHeader();
        }
    });

    $('#return-header').click(function() {
        showHeader();
    });
});
