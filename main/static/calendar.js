var open_qtip;

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

function datecell_qtip_content() {
    // MAKE SURE YOUR SELECTOR MATCHES SOMETHING IN YOUR HTML!!!
    $('td').each(function() {
        var id='div_' + $(this).attr('id');
        $(this).qtip({
            content: {
               // text: "custom text",
                text: $('#' + id),
                title: {
                    text: 'Create New Goal Entry',
                    button: 'Close' // Close button
              },  
            },  
            style: { 
                classes: 'qtip-blue qtip-rounded'
            },
           hide: true, // Don't hide on any event except close button
           show:  'click'
        }); 
    }); 
}

function register_new_goal_handler() {
    $("#create_new_goal").submit(submit_new_goal);
    $(".goal_entry_form").bind('submit', submit_new_goal_entry);
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

function submit_new_goal_entry(eventObject) {
    form = $(eventObject.target);
    $.post("", form.serialize(), function (data, textStatus, jqXHR) {
        if (jqXHR.getResponseHeader('X-addNewGoalEntryStatus') == 'success') {
            goalSelect = form.find('select[name="goal"]');
            goalid = goalSelect.val();
            goalname = goalSelect.find('option[value="' + goalid + '"]').text()
            starcolor = form.find('select[name="starcolor"]').val();
            entrydate = form.find('input[name="entrydate"]').val();
            goalentry = form.find('textarea[name="desc"]').val()
            goalcolor = $('#goal-tab-' + goalid).attr('goalcolor');

            var container_id = 'div_' + open_qtip
            $('#' + open_qtip).qtip('hide');
            var daySelector = '#' + open_qtip;
            var dayStarSelector = daySelector + ' .star-' + goalid;
            var dayStarColorSelector = dayStarSelector + ' .star-value-' + starcolor;
            var dayStarAnySelector = dayStarSelector + ' .summary-star';

            var file = 'foo';
            switch (starcolor) {
                case '1':
                    file = "/static/stars/bronze.png";
                    break;
                case '2':
                    file = "/static/stars/silver.png";
                    break;
                case '3':
                    file = "/static/stars/gold.png";
                    break;
            }

            if ($(dayStarSelector).length == 0) {
                // There's no star on this day for this goal, so just add it.
                $(daySelector).append("<div class='calendar-star star-"+goalid+"'><img class='summary-star star-value-"+starcolor+"' src='"+file+"'></div>").children(':last').show();
            } else if ($(dayStarColorSelector).length == 0) {
                // There is a star on this day for this goal, but it's the wrong color, so we need to update it.
                star = $(dayStarAnySelector);
                star.removeClass('star-value-1 star-value-2 star-value-3');
                star.addClass('star-value=' + starcolor);
                star.attr('src', file);
            }

            wallday = $('#wall-day-' + entrydate);
            var hadDay = true;
            if (wallday.length == 0) {
                var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                var date = new Date(entrydate);
                hadDay = false;
                wallday = $("<div id='wall-day-"+entrydate+"' class='wall-day' date='"+entrydate+"''><div>"+months[date.getUTCMonth()] + " " + date.getUTCDate() + "</div></div>");
                wallday.hide();
                var added = false;
                $('.wall-day').each(function () {
                    if ($(this).attr('date') < entrydate) {
                        added = true;
                        wallday.insertBefore($(this));
                        return false;
                    }
                });
                if (!added) {
                    $('#wall-data').append(wallday);
                }
            }
            entry = $("<div id='wall-entry'>" +
                        "<img class='summary-star wall-star' src='"+file+"'>" +
                        "<div class='goal-wall-entry'>" +
                        "[<span class='goal-color-"+goalcolor+"'>"+goalname+"</span>] " +
                        "</div>" +
                        "<div class='goal-wall-entry'>" +
                        goalentry +
                        "</div>" +
                        "<div class='cleardiv'></div>" +
                        "</div> ");
            wallday.append(entry.hide());
            if (hadDay) {
                entry.slideDown();
            } else {
                entry.show();
                wallday.slideDown();
            }
                
        } else {
            var container_id = 'div_' + open_qtip
            console.log($('#' + container_id));
            $('#' + container_id).html(data);
            console.log("In the failed case");
            $('#' + container_id).show();
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
        goalid = $(this).attr('goalid');
        $('.calendar-star').hide();
        $('.star-' + goalid).show();
        $('.goal_entry_form').hide();
        $('.entry_form_' + goalid).show();
    }
}

$(function () {
    qtip_content();
    datecell_qtip_content();
    register_new_goal_handler();

    $('.goal-tab').click(tab_click_handler);
    $('.goal-tab').first().trigger('click');
    $('.datecell').click(function () {
        $('.datecell').removeClass('selected-datecell');
        $(this).addClass('selected-datecell');
    	
		if(open_qtip != undefined) {
			console.log("open qtip is : " + open_qtip);
			$('#' + open_qtip).qtip('hide');
		}
		open_qtip =  $(this).attr('id');
		$('#' + open_qtip).show();
	});
});
