$(document).ready(function() {
    $('#id_new_username').val(oldInfo.username);
    $('#id_new_name').val(oldInfo.name);
    $('#id_new_email').val(oldInfo.email);
    $('#id_new_bio').val(oldInfo.bio);
    $('#id_new_website').val(oldInfo.website);
    console.log(oldInfo.website)

    $('#new-default-city').selectivity({
        allowClear: true,
        items: cityNames,
        placeholder: 'Default location',
        value: oldInfo.default_city_id,
    });

    $('#change-info-form').submit(function() {
        var newDefaultCityData = $('#new-default-city').selectivity('data');
        $('#new-default-city-input-hidden').val(JSON.stringify(newDefaultCityData));
        return true;
    });
});
