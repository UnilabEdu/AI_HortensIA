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


function updateLeaderboardColors(chart, userRank) {
    if (userRank > 10) {
        chart.data.datasets[0].backgroundColor.push(leaderboardSpecialGradient)
    } else {
        chart.data.datasets[0].backgroundColor[userRank-1] = leaderboardSpecialGradient
    }
    chart.update()
}


// var monthChartHTML = document.getElementById('monthChart')
//
// monthChartHTML.addEventListener('load', (function() {

// W
// updateChartData(monthChart, labelsNew, dataNew);


// }))



var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    return await response.json()
};

async function renderActivityCharts() {
    let ctx;
        activityData = await fetchActivityData();
        let heatmapData = activityData.heatmap_data
        let monthLabels = activityData.month_chart_labels
        let monthData = activityData.month_chart_frequencies
        let weekLabels = activityData.month_chart_labels.slice(-7)
        let weekData = activityData.month_chart_frequencies.slice(-7)
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

    var buttonAnytime = document.getElementById('btn-radar-anytime')
    var buttonMonth = document.getElementById('btn-radar-month')
    var buttonWeek = document.getElementById('btn-radar-week')
    var buttonDay = document.getElementById('btn-radar-day')

    updateRadar(radarChartAnytimePrimary, [data.user_anytime_primary, data.everyone_anytime_primary])
    updateRadar(radarChartAnytimeSecondary, [data.user_anytime_secondary, data.everyone_anytime_secondary])

    buttonAnytime.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_anytime_primary, data.everyone_anytime_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_anytime_secondary, data.everyone_anytime_secondary])
        console.log('ANYTIME')
    })

    buttonMonth.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_month_primary, data.everyone_month_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_month_secondary, data.everyone_month_secondary])
        console.log('MONTH')
    })

    buttonWeek.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_week_primary, data.everyone_week_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_week_secondary, data.everyone_week_secondary])
        console.log('WEEK')

    })

    buttonDay.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_day_primary, data.everyone_day_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_day_secondary, data.everyone_day_secondary])
        console.log('DAY')
    })

    // var ctx;
    // console.log(data.user_anytime_primary)
    // console.log(data.everyone_anytime_primary)
    // updateRadar(radarChartAnytimePrimary, [data.user_anytime_primary, data.everyone_anytime_primary])
    // updateRadar(radarChartAnytimeSecondary, [data.user_anytime_secondary, data.everyone_anytime_secondary])
    // updateRadar(radarChartMonthPrimary, [data.user_month_primary, data.everyone_month_primary])
    // updateRadar(radarChartMonthSecondary, [data.user_month_secondary, data.everyone_month_secondary])
    // updateRadar(radarChartWeekPrimary, [data.user_week_primary, data.everyone_week_primary])
    // updateRadar(radarChartWeekSecondary, [data.user_week_secondary, data.everyone_week_secondary])
    // updateRadar(radarChartDayPrimary, [data.user_day_primary, data.everyone_day_primary])
    // updateRadar(radarChartDaySecondary, [data.user_day_secondary, data.everyone_day_secondary])











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
    return await response.json();
};

async function renderLeaderboardChart() {
    fetchedData = await fetchLeaderboardData();
    let leaderboardLabels = fetchedData.leaderboard_labels
    let leaderboardData = fetchedData.leaderboard_data
    let userRank = fetchedData.current_user_rank
    updateChartData(leaderboardChart, leaderboardLabels, leaderboardData)
    updateLeaderboardColors(leaderboardChart, userRank)
}

renderLeaderboardChart()
