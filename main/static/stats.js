/* Prints Stacked Bar Chard for Summary page. */
function PrintStackedBarChart(data_gold, data_silver, data_bronze, labels){
    $('#chart').html('');
    plot3 = $.jqplot('chart', [data_gold, data_silver, data_bronze], {
        stackSeries: true,
	title: 'Goal Summary',
	axes:{
		xaxis: {
			label:'Goals',
		},
		yaxis : {
			label: 'Stars',
		}
	},
	seriesColors:['#FDD017', '#C0C0C0', '#CD7F32'],
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {
                highlightMouseDown: true   
            },
            pointLabels: {show: true}
        },
    });
};

/* Prints Pie char for individual goal. */
function PrintPieChart(data_gold, data_silver, data_bronze, goal_name){
    console.log("Pie print");
	var data = [
		['Gold', 3], ['Silver', 5], ['Bronze', 3]
	];
//    plot1 = $.jqplot('chart1', [data_gold, data_silver, data_bronze], {
    plot1 = $.jqplot('chart', [data], {
	title: goal_name,
	seriesColors:['#FDD017', '#C0C0C0', '#CD7F32'],
        seriesDefaults:{
            shadow: true,
            renderer:$.jqplot.PieRenderer,
            rendererOptions: {
		showDataLabels: true
            },
            pointLabels: {show: true}
        },
    });
};
