// Create the tooltips only when document ready
 $(document).ready(function()
 {
	// MAKE SURE YOUR SELECTOR MATCHES SOMETHING IN YOUR HTML!!!
	$('a').each(function() {
		$(this).qtip({
			content: {
                 		text: $(this).next('.tooltiptext'),
      				title: {
         				text: 'Create New Goal',
         				button: 'Close' // Close button
      				},
             		},
   			hide: false // Don't hide on any event except close button
         });
     });
 });
