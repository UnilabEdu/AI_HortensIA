function updateChartData(chart, label, data) {
    chart.data.labels = label
    chart.data.datasets.forEach((dataset) => {
        dataset.data = data;
    });
    chart.update();
}

// function updateLeaderboard(chart, label, data) {
//     chart.data.labels = label
//     chart.data.datasets.forEach((dataset) => {
//         dataset.data = data;
//     });
//     chart.update();
// }

function updateRadar(chart, data) {
    var count = 0
    chart.data.datasets.forEach((dataset) => {
        if (count === 0) {
            dataset.data = data[0];
            count++
        } else {
            dataset.data = data[1]
        }
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

// W
// updateChartData(monthChart, labelsNew, dataNew);


// }))



var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    allActivityData = await response.json();
    return allActivityData
};

async function renderActivityCharts() {
    let ctx;
        data = await fetchActivityData();
        let heatmapData = data.heatmap_data
        let monthLabels = data.month_chart_labels
        let monthData = data.month_chart_frequencies
        let weekLabels = data.month_chart_labels.slice(-7)
        let weekData = data.month_chart_frequencies.slice(-7)
        updateHeatmap(heatmapChart, heatmapData)
        updateChartData(monthChart, monthLabels, monthData);
        updateChartData(weekChart, weekLabels, weekData)
        var buttonWeek = document.getElementById('btn-activity-chart-week')
        var buttonMonth = document.getElementById('btn-activity-chart-month')


        buttonWeek.addEventListener("click", function () {
                    updateChartData(monthChart, weekLabels, weekData)
        })

        buttonMonth.addEventListener("click", function () {
                    updateChartData(monthChart, monthLabels, monthData)
        })
}

renderActivityCharts()


var fetchRadarData = async function () {
    var response = await fetch('/dashboard/getradarsdata');
    allRadarData = await response.json();
    return allRadarData
};

async function renderRadarCharts() {
    data = await fetchRadarData();

    // var ctx;
    console.log(data.user_anytime_primary)
    console.log(data.everyone_anytime_primary)
    updateRadar(radarChartAnytimePrimary, [data.user_anytime_primary, data.everyone_anytime_primary])
    updateRadar(radarChartAnytimeSecondary, [data.user_anytime_secondary, data.everyone_anytime_secondary])

    // ctx = document.getElementById("radarChartAnytimePrimary").getContext('2d');
    // var radarChartAnytimePrimary = new Chart(ctx, JSON.parse(data.primary_anytime_chart));


    // ctx = document.getElementById("radarChartAnytimeSecondary").getContext('2d');
    // var radarChartAnytimeSecondary = new Chart(ctx, JSON.parse(data.secondary_anytime_chart));


    // ctx = document.getElementById("radarChartMonthPrimary").getContext('2d');
    // var radarChartMonthPrimary = new Chart(ctx, JSON.parse(data.primary_month_chart));
    //
    //
    // ctx = document.getElementById("radarChartMonthSecondary").getContext('2d');
    // var radarChartMonthSecondary = new Chart(ctx, JSON.parse(data.secondary_month_chart));
    //
    //
    // ctx = document.getElementById("radarChartWeekPrimary").getContext('2d');
    // var radarChartWeekPrimary = new Chart(ctx, JSON.parse(data.primary_week_chart));
    //
    //
    // ctx = document.getElementById("radarChartWeekSecondary").getContext('2d');
    // var radarChartWeekSecondary = new Chart(ctx, JSON.parse(data.secondary_week_chart));
    //
    //
    // ctx = document.getElementById("radarChartDayPrimary").getContext('2d');
    // var radarChartDayPrimary = new Chart(ctx, JSON.parse(data.primary_day_chart));
    //
    //
    // ctx = document.getElementById("radarChartDaySecondary").getContext('2d');
    // var radarChartDaySecondary = new Chart(ctx, JSON.parse(data.secondary_day_chart));

}

renderRadarCharts()



var fetchLeaderboardData = async function () {
    var response = await fetch('/dashboard/getleaderboarddata');
    leaderboardData = await response.json();
    return leaderboardData
};

async function renderLeaderboardChart() {
    data = await fetchLeaderboardData();
    let leaderboardLabels = data.leaderboard_labels
    let leaderboardData = data.leaderboard_data
    updateChartData(leaderboardChart, leaderboardLabels, leaderboardData)

}

renderLeaderboardChart()
