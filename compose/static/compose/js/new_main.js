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
    console.log(tagNames);

    //
    // $('#intentions-input').selectivity({
    //     // allowClear: true,
    //     items: ['Amsterdam', 'Antwerp'/*, ...*/],
    //     placeholder: 'No city selected',
    //     multiple: true,
    //     inputType: 'Multiple',
    //     placeholder: 'Intentions',
    //     createTokenItem: function(val) {
    //         return {
    //             id: val,
    //             text: val,
    //         }
    //     }
    // });

    $('#new-form').submit(function() {
        data = $('#tags').selectivity('data');
        $('#tags-input-hidden').val(JSON.stringify(data));
        return true;
    });
});
