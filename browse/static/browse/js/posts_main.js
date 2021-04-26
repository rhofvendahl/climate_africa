$(document).ready(function() {
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
