var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    allActivityData = await response.json();
    return allActivityData
};

async function renderActivityCharts() {
    data = await fetchActivityData();

    var ctx;
    console.log(JSON.parse(JSON.stringify(data.week_chart)))

    ctx = document.getElementById("weekChart").getContext('2d');
    var weekChart = new Chart(ctx, JSON.parse(JSON.stringify(data.week_chart)));

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
    console.log(JSON.parse(JSON.stringify(data.primary_anytime_chart)))
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
