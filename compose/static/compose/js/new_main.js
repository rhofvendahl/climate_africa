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
        var tagsData = $('#tags').selectivity('data');
        $('#tags-input-hidden').val(JSON.stringify(tagsData));
        var cityData = $('#city').selectivity('data');
        $('#city-input-hidden').val(JSON.stringify(cityData));
        return true;
    });
});
