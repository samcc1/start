
function qtip_content() {
    // MAKE SURE YOUR SELECTOR MATCHES SOMETHING IN YOUR HTML!!!
    $('#create_new_goal2').each(function() {
        $(this).qtip({
            content: {
                text: $('#new_goal_container'),
                title: {
                    text: 'Create New Goal',
                    button: 'Close' // Close button
                },
            },
            style: { 
                classes: 'qtip-blue qtip-rounded'
            },
            show: 'click',
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
            goalTitle = $("#id_title").val();
            $("#new_goal_container").html(data);
            $('#create_new_goal2').qtip('hide');
            register_new_goal_handler();
            $("<div class='goal-tab'>"+goalTitle+"</div>").insertBefore("#create_new_goal2").click(tab_click_handler);
        } else {
            $("#new_goal_container").html(data);
            $("#new_goal_container").show();
            register_new_goal_handler();
        }   
    }); 
    return false;
}

function tab_click_handler() {
    if ($(this).attr('id') != 'create_new_goal2') {
        $('.goal-tab').removeClass('selected-tab');
        $(this).addClass('selected-tab');
        // select the goal for this tab
    }
}

$(function () {
    qtip_content();
    register_new_goal_handler();

    $('.goal-tab').click(tab_click_handler);
    $('.goal-tab').first().trigger('click');
    $('.datecell').click(function () {
        $('.datecell').removeClass('selected-datecell');
        $(this).addClass('selected-datecell');
    });
});
