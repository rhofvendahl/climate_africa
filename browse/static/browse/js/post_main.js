$(document).ready(function() {
    if (reportImpactTagNames) {
        $('#report-impacts').selectivity({
            value: reportImpactTagNames,
            multiple: true,
            readOnly: true,
        });
    }

    if (projectIntentionTagNames) {
        $('#project-intentions').selectivity({
            value: projectIntentionTagNames,
            multiple: true,
            readOnly: true,
        });
    }
});
