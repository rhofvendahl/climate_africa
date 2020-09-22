$(document).ready(function() {
    var viewAll = false;
    $('#continued').hide()


    var renderDefaultCity = function() {
        $('#default-city').selectivity({
            allowClear: true,
            items: cityNames,
            placeholder: 'Default location',
        });
    }

    var renderPersonContinued = function() {
        $('#initial').hide();
        $('#continued').show();
        renderDefaultCity();
    }

    var renderOrganizationContinued = function() {
        $('#initial').hide();
        $('#continued').show();
        renderDefaultCity();
    }

    var renderPersonAll = function() {
        $('#initial').show();
        $('#continue-button').hide();
        $('#continued').show();
    }

    var renderOrganizationAll = function() {
        $('#initial').show();
        $('#continue-button').hide();
        $('#continued').show();
    }

    $('#continue-button').click(function() {
        if ($('#id_is_organization').is(':checked')) {
            renderOrganizationContinued();
        } else {
            renderPersonContinued();
        }
    });

    $('#id_is_organization').change(function() {
        if ($('#id_is_organization').is(':checked')) {
            renderOrganizationAll();
        } else {
            renderPersonAll();
        }
    });

    $('#trigger-submission-button').click(function() {
        if ($('#id_is_organization').is(':checked')) {
            renderOrganizationAll();
        } else {
            renderPersonAll();
        }
        viewAll = true;
        $('#submit-button-hidden').trigger('click');
    });
});
