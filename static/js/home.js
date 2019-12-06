$(document).ready(function() {
    $('#trigger1').click(function() {
        console.log('Yahoooo!!!');
        $('.btn-primary').removeClass('btn-primary').addClass('btn-success');
        $('#test-1').append('<button class="btn btn-primary" id="trigger3">Trigger3</button>')
    });

    $('body').on('click', '#trigger2', function() {
        console.log('Yahoooo!!!');
        $('.btn-primary').removeClass('btn-primary').addClass('btn-success');
        $('#test-1').find('button').remove()
    });
    
    $('body').on('keyup', 'input[name="input-1"]', function(event) {
        console.log('event', event);
        // $('#test-1').append(event.key)
        var text = $('#test-1').text();
        console.log(text);
        text += event.key;
        console.log(text);
        $('#test-1').text(text);
    });

    $('body').on('change', '#select-1', function(event) {
        var url = $(this).attr('data-url');
        url = url.replace('placeholder', $(this).val());
        console.log($(this).val())
        $.ajax({
            url: url,
            method: 'GET',
            data: {
                var: 'TEST'
            },
            success: function(data) {
                console.log(data);
                if(data.status == true) {
                    $('#results-wrapper').html(data.message);
                }
            },
            error: function(error) {
                console.log(error);
            },
            complete: function() {}
        });
    })
});