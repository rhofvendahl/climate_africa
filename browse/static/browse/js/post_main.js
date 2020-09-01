$(document).ready(function() {
    $('#tags').selectivity({
        value: tagNames,
        multiple: true,
        readOnly: true,
    });
    console.log(tagNames);
});
