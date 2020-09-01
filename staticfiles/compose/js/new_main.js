$(document).ready(function() {
    $('#intentions-input').selectivity({
        items: {{ tag_names }},
        multiple: true,
        inputType: 'Multiple',
        placeholder: 'Intentions',
        createTokenItem: function(val) {
            return {
                id: val,
                text: val,
            }
        }
    });

    // $('#triage-form').submit(function() {
    //     data = $('#tags').selectivity('data');
    //     console.log(data);
    //     $('#tags-input').val(JSON.stringify(data));
    //     return true;
    // });
});
