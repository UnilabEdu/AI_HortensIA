    // ctx = document.getElementById("monthChart").getContext('2d');
    // var monthChart = new Chart(ctx, JSON.parse(data.month_chart));
    //

    ctx = document.getElementById("monthChart").getContext('2d');
    const monthChart = new Chart(ctx, JSON.parse('{"type": "line", "data": {"labels": ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"], "datasets": [{"label": "Tickets Filed Last 30 Days", "data": ["1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2"], "borderColor": "rgba(93, 65, 145, 1)", "borderWidth": 2, "backgroundColor": "rgba(127, 92, 194, 1)", "tension": 0.4, "fill": true}]}, "options": {"elements": {"point": {"radius": 0, "hitRadius": 25}}, "scales": {"y": {"beginAtZero": true, "grid": {"display": false, "drawBorder": false, "tickMarkLength": 0}}, "x": {"grid": {"display": false, "drawBorder": false, "tickMarkLength": 0}}}, "plugins": {}}}'
));

    var labelsNew = ["Why", "u", "no", "work", "???"];
    var dataNew = [2, 4, 5, 6, 10];



function updateChartData(chart, label, data) {
    chart.data.labels = label
    chart.data.datasets.forEach((dataset) => {
        dataset.data = data;
    });
    chart.update();
}

function updateHeatmap(heatmap, dataNew) {
    heatmap.data.datasets[0].data = dataNew;
    heatmap.update();
}


// var monthChartHTML = document.getElementById('monthChart')
//
// monthChartHTML.addEventListener('load', (function() {
updateChartData(monthChart, labelsNew, dataNew);
// }))



var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    allActivityData = await response.json();
    return allActivityData
};

async function renderActivityCharts() {
    var ctx;
        data = await fetchActivityData();
        heatmapData = data.heatmap_data

        updateHeatmap(heatmapChart, heatmapData)


    // function updateChartData(chart, label, data) {
    //     chart.data.labels.push(label);
    //     chart.data.datasets.forEach((dataset) => {
    //         dataset.data.push(data);
    //     });
    //     chart.update();
    // }
    //
    // function removeData(chart) {
    //     chart.data.labels.pop();
    //     chart.data.datasets.forEach((dataset) => {
    //         dataset.data.pop();
    //     });
    //     chart.update();
    // }
    //
    //
    // removeData(monthChart)
    //
    // updateChartData(monthChart, JSON.parse(data.month_chart).data.labels, JSON.parse(data.month_chart).data.datasets[0].data)
    //


    updateChartData(monthChart, JSON.parse(data.month_chart).data.labels, JSON.parse(data.month_chart).data.datasets[0].data);


    ctx = document.getElementById("weekChart").getContext('2d');
    var weekChart = new Chart(ctx, JSON.parse(data.week_chart));

    ctx = document.getElementById("leaderboardChart").getContext('2d');
    var leaderboardChart = new Chart(ctx, JSON.parse(data.leaderboard_chart));

}

renderActivityCharts()




var fetchRadarData = async function () {
    var response = await fetch('/dashboard/getradarsdata');
    allRadarData = await response.json();
    return allRadarData
};

async function renderRadarCharts() {
    data = await fetchRadarData();

    var ctx;

    ctx = document.getElementById("radarChartAnytimePrimary").getContext('2d');
    var radarChartAnytimePrimary = new Chart(ctx, JSON.parse(data.primary_anytime_chart));


    ctx = document.getElementById("radarChartAnytimeSecondary").getContext('2d');
    var radarChartAnytimeSecondary = new Chart(ctx, JSON.parse(data.secondary_anytime_chart));


    ctx = document.getElementById("radarChartMonthPrimary").getContext('2d');
    var radarChartMonthPrimary = new Chart(ctx, JSON.parse(data.primary_month_chart));


    ctx = document.getElementById("radarChartMonthSecondary").getContext('2d');
    var radarChartMonthSecondary = new Chart(ctx, JSON.parse(data.secondary_month_chart));


    ctx = document.getElementById("radarChartWeekPrimary").getContext('2d');
    var radarChartWeekPrimary = new Chart(ctx, JSON.parse(data.primary_week_chart));


    ctx = document.getElementById("radarChartWeekSecondary").getContext('2d');
    var radarChartWeekSecondary = new Chart(ctx, JSON.parse(data.secondary_week_chart));


    ctx = document.getElementById("radarChartDayPrimary").getContext('2d');
    var radarChartDayPrimary = new Chart(ctx, JSON.parse(data.primary_day_chart));


    ctx = document.getElementById("radarChartDaySecondary").getContext('2d');
    var radarChartDaySecondary = new Chart(ctx, JSON.parse(data.secondary_day_chart));

}

renderRadarCharts()
