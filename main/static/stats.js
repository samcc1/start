$(function(){
    var s1 = [2, 6, 7, 10];
    var s2 = [7, 5, 3, 2];
    var s3 = [14, 9, 3, 8];
    plot3 = $.jqplot('chart', [s1, s2, s3], {
        stackSeries: true,
        //captureRightClick: true,
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {
                highlightMouseDown: true   
            },
            pointLabels: {show: true}
        },
        legend: {
            show: true,
            location: 'e',
            placement: 'outside'
        }      
    });
 
    //$('#chart').bind('jqplotDataRightClick', 
    //    function (ev, seriesIndex, pointIndex, data) {
    //        $('#info3').html('series: '+seriesIndex+', point: '+pointIndex+', data: '+data);
    //    }
    //); 
});
