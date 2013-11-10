
function PrintStackedBarChart(data_gold, data_silver, data_bronze){
    console.log(data_gold);
    plot3 = $.jqplot('chart', [data_gold, data_silver, data_bronze], {
        stackSeries: true,
        //captureRightClick: true,
	seriesColors:['#FDD017', '#C0C0C0', '#CD7F32'],
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {
                highlightMouseDown: true   
            },
            pointLabels: {show: true}
        },
//       legend: {
//            show: true,
//            location: 'e',
//            placement: 'outside'
//        }      
    });
 
    //$('#chart').bind('jqplotDataRightClick', 
    //    function (ev, seriesIndex, pointIndex, data) {
    //        $('#info3').html('series: '+seriesIndex+', point: '+pointIndex+', data: '+data);
    //    }
    //); 
};
