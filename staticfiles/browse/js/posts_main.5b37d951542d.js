// $(document).ready(function() {
//
//     var animating = false;
//
//     var hideHeader = function() {
//         if (!animating) {
//             animating = true;
//             // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
//             $('#header').animate({top: '-2.5rem'}, 400, function() {
//                 $('#header').hide();
//                 animating = false;
//             });
//             $('#return-header').show();
//             $('#return-header').animate({marginTop: ".7rem"}, 400);
//             // headerHidden = true;
//         }
//     }
//
//     var showHeader = function() {
//         if (!animating) {
//             $('#header').show();
//             animating = true;
//             // THESE REM VALUES ARE DEPENDENT ON STYLESHEET - not ideal.
//             $('#header').animate({top: '3rem'}, 400, function() {
//                 animating = false;
//             });
//             $('#return-header').animate({marginTop: "-2.5rem"}, 400, function() {
//                 $('#return-header').hide();
//             });
//             // headerHidden = false;
//         }
//     }
//     //
//     // var animating = false;
//     // var shouldHide = false;
//     // var shouldShow = false;
//     //
//     // var hideHeader = function() {
//     //     if ($('#header').is(':visible')) {
//     //         $('#header').animate({top: '-2.5rem'}, function() {
//     //             $('#header').hide();
//     //             headerHidden = true; // in case things have changed (somehow)
//     //         });
//     //     }
//     //     // headerHidden = true;
//     // }
//     //
//     // var showHeader = function() {
//     //     if (headerHidden) {
//     //         $('#header').show();
//     //         $('#header').animate({top: '3rem'}, function() {
//     //             headerHidden = false; // in case things have changed (somehow)
//     //         });
//     //     }
//     //     // headerHidden = false;
//     // }
//
//     // var lastScrollTop = 0;
//     // var headerHidden = false;
//     // $('#browse').scroll(function(event) {
//     //     var scrollTop = $(this).scrollTop();
//     //     if (scrollTop > lastScrollTop) {
//     //         // console.log('downscroll');
//     //         if (!headerHidden) {
//     //             hideHeader();
//     //             headerHidden = true;
//     //         }
//     //         // $('#header').hide();
//     //         // $('#header').addClass('header-hide', 1000);
//     //         // $('#phone-mockup').addClass('header-hide', 1000);
//     //     } else {
//     //         // console.log('upscroll');
//     //         if (headerHidden) {
//     //             showHeader();
//     //             headerHidden = false;
//     //         }
//     //         // $('#header').show();
//     //         // $('#header').removeClass('header-hide', 1000);
//     //     }
//     //     lastScrollTop = scrollTop;
//     // });
//
//     // Firefox
//     $('html').on('DOMMouseScroll', function(event) {
//         var delta = event.originalEvent.detail;
//
//         if (delta > 0) {
//             // console.log('scrollup', headerHidden);
//             showHeader();
//         } else {
//             // console.log('scrolldown', headerHidden);
//             hideHeader(0);
//         }
//     });
//
//     // Chrome, IE, Opera, Safari (& hopefully others)
//     $('html').on('mousewheel', function(event) {
//         var delta = event.originalEvent.wheelDelta;
//
//         if (delta > 0) {
//             // console.log('scrollup', animating);
//             showHeader();
//         } else {
//             // console.log('scrolldown', animating);
//             hideHeader();
//         }
//     });
// });

$(document).ready(function() {
    // Kludgey; starts out with expanded, to get expanded height; replace when possible
    var initialFooterHeight = $('#posts-footer').height();
    // $('#browse-footer').css({height: '4rem'});

    var expand = function() {
        $('#search-expand-icon-wrapper').hide();
        $('#search-collapse-icon-wrapper').show();

        $('.bar-extra').show();

        $('#posts-footer').animate({height: '19.2rem'}, 250); // previously 15.4. calculated from css.
    }

    var collapse = function() {
        $('#search-collapse-icon-wrapper').hide();
        $('#search-expand-icon-wrapper').show();

        $('#posts-footer').animate({height: '4rem'}, 250, function() {
            $('.bar-extra').hide();
        });
    }
    collapse();

    $('#search-expand-icon-wrapper').click(function() {
        expand();
    });

    $('#search-collapse-icon-wrapper').click(function() {
        collapse();
    });

    $('#city').selectivity({
        allowClear: true,
        items: availableCityNames,
        placeholder: 'Location',
    });

    $('#id_type').change(function() {
        $('#id_type').css({'color': '#EEEEEE'});
    });

    $('#id_sort_by').change(function() {
        $('#id_sort_by').css({'color': '#EEEEEE'});
    });

    $('#search-form').submit(function() {
        var cityData = $('#city').selectivity('data');
        $('#city-input-hidden').val(JSON.stringify(cityData));
        return true;
    });
});
