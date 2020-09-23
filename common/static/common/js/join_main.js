$(document).ready(function() {
    $('#additional-info-mat').hide();
    // var viewAll = false;
    // $('#continued').hide()
    //
    //

    var renderDefaultCity = function() {
        $('#default-city').selectivity({
            allowClear: true,
            items: cityNames,
            placeholder: 'Default location',
        });
    }

    var renderPersonFields = function() {
        $('#additional-info-mat').show();
        $('#id_name').attr({'placeholder': 'Full name'})
        renderDefaultCity();
    }

    var renderOrganizationFields = function() {
        $('#additional-info-mat').show();
        $('#id_name').attr({'placeholder': 'Organization name'})
        renderDefaultCity();
    }

    var render = function() {
        var val = $('#id_is_organization').val();
        if (val == '') {
            $('#additional-info-mat').hide();
        } else if (val == 'False') {
            renderPersonFields();
        } else if (val == 'True') {
            renderOrganizationFields();
        }
    }
    render()

    // var renderPersonAll = function() {
    //     $('#initial').show();
    //     $('#continue-button').hide();
    //     $('#continued').show();
    // }
    //
    // var renderOrganizationAll = function() {
    //     $('#initial').show();
    //     $('#continue-button').hide();
    //     $('#continued').show();
    // }
    //
    // $('#continue-button').click(function() {
    //     if ($('#id_is_organization').is(':checked')) {
    //         renderOrganizationContinued();
    //     } else {
    //         renderPersonContinued();
    //     }
    // });
    //

    $('#id_is_organization').change(function() {
        render()
        // if ($('#id_is_organization').is(':checked')) {
        //     renderOrganizationAll();
        // } else {
        //     renderPersonAll();
        // }
    });

    // $('#trigger-submission-button').click(function() {
    //     if ($('#id_is_organization').is(':checked')) {
    //         renderOrganizationAll();
    //     } else {
    //         renderPersonAll();
    //     }
    //     viewAll = true;
    //     $('#submit-button-hidden').trigger('click');
    // });
    $('#join-form').submit(function() {
        var defaultCityData = $('#default-city').selectivity('data');
        $('#default-city-input-hidden').val(JSON.stringify(defaultCityData));
        return true;
    });
});
