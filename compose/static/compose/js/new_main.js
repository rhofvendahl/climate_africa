$(document).ready(function() {
    if (defaultCityObject) {
        $('#city').selectivity({
            allowClear: true,
            items: cityNames,
            placeholder: 'Location',
            data: defaultCityObject,
        });
    } else {
        $('#city').selectivity({
            allowClear: true,
            items: cityNames,
            placeholder: 'Location',
        });
    }

    $('#report-type').selectivity({
        allowClear: true,
        items: reportTypeNames,
        placeholder: 'Report type',
    });

    $('#report-impacts').selectivity({
        items: reportImpactNames,
        multiple: true,
        inputType: 'Multiple',
        placeholder: 'Report impacts ("Enter" to create)',
        createTokenItem: function(val) {
            return {
                id: val,
                text: val,
            }
        }
    });

    $('#project-intentions').selectivity({
        items: projectIntentionNames,
        multiple: true,
        inputType: 'Multiple',
        placeholder: 'Project intentions ("Enter" to create)',
        createTokenItem: function(val) {
            return {
                id: val,
                text: val,
            }
        }
    });

    $('#new-form').submit(function() {
        var tagsData = $('#tags').selectivity('data');
        $('#tags-input-hidden').val(JSON.stringify(tagsData));
        var cityData = $('#city').selectivity('data');
        $('#city-input-hidden').val(JSON.stringify(cityData));
        return true;
    });

    var hideAll = function() {
        $('#report-meta-mat').hide();
        $('#project-meta-mat').hide();
        $('#event-meta-mat').hide();
        $('#well-meta-mat').hide();
    }

    var render = function() {
        hideAll();
        var val = $('#id_type').val();
        if (val == 'extreme_weather_report') {
            $('#report-meta-mat').show();
        } else if (val == 'resilience_project') {
            $('#project-meta-mat').show();
        } else if (val == 'climate_justice_event') {
            $('#event-meta-mat').show();
        } else if (val == 'well_needed') {
            $('#well-meta-mat').show();
        }
    }
    render();

    $('#id_type').change(function() {
        render();
    });

    $('#new-form').submit(function() {
        var cityData = $('#city').selectivity('data');
        $('#city-input-hidden').val(JSON.stringify(cityData));
        var reportTypeData = $('#report-type').selectivity('data');
        $('#report-type-input-hidden').val(JSON.stringify(reportTypeData));
        var reportImpactsData = $('#report-impacts').selectivity('data');
        $('#report-impacts-input-hidden').val(JSON.stringify(reportImpactsData));
        var projectIntentionsData = $('#project-intentions').selectivity('data');
        $('#project-intentions-input-hidden').val(JSON.stringify(projectIntentionsData));
        return true;
    });
});
