function qtip_content() {
    // MAKE SURE YOUR SELECTOR MATCHES SOMETHING IN YOUR HTML!!!
    $('#create_new_goal2').each(function() {
        $(this).qtip({
            content: {
                text: $(this).next('.tooltiptext'),
                title: {
                    text: 'Create New Goal',
                    button: 'Close' // Close button
                },
            },
            style: { 
                name: 'dark' // Inherit from preset style
            },
            hide: false // Don't hide on any event except close button
        });
    });
}

function register_new_goal_handler() {
    $("#create_new_goal").submit(submit_new_goal);
}


function submit_new_goal() {
    $.post("", $("#create_new_goal").serialize(), function (data, textStatus, jqXHR) {
        if (jqXHR.getResponseHeader('X-addNewGoalStatus') == 'success') {
            $("#new_goal_container").html(data);
            $('a').qtip('hide');
            register_new_goal_handler();
            // TODO - Add in a new goal tab to calendar
        } else {
            $("#new_goal_container").html(data);
            $("#new_goal_container").show();
            register_new_goal_handler();
        }   
    }); 
    return false;
}

$(function () {
    qtip_content();
    register_new_goal_handler();
});

