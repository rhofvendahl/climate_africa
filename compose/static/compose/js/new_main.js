$(document).ready(function() {
    $('#tags').selectivity({
        items: tagNames,
        multiple: true,
        inputType: 'Multiple',
        placeholder: 'Intentions ("Enter" to create)',
        createTokenItem: function(val) {
            return {
                id: val,
                text: val,
            }
        }
    });

    $('#city').selectivity({
        allowClear: true,
        items: cityNames,
        placeholder: 'Location',
    });

    $('#new-form').submit(function() {
        console.log('hey')
        tags_data = $('#tags').selectivity('data');
        $('#tags-input-hidden').val(JSON.stringify(tags_data));
        city_data = $('#city').selectivity('data');
        console.log('city data', city_data)
        $('#city-input-hidden').val(JSON.stringify(city_data));
        return true;
    });
});
