var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    allActivityData = await response.json();
    return allActivityData
};

async function renderActivityCharts() {
    data = await fetchActivityData();

    var ctx;
    heatmapData = data.heatmap_data
                Utils.load(() => {
                    Chart.defaults.fontSize = 9;
                    let ctx = document.getElementById('heatmapChart').getContext('2d');
                    window.myMatrix = new Chart(ctx, {
                        type: 'matrix',
                        data: {
                            datasets: [{
                                label: 'Activity Heatmap',
                                data: heatmapData,
                                backgroundColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 8;
                                    const alpha = (10 + value) / 60;
                                    return Chart.helpers.color('#7E57C2').alpha(alpha).lighten(0.1 / c.dataset.data[c.dataIndex].v).rgbString();
                                },
                                borderColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 8;
                                    const alpha = (10 + value) / 60;
                                    return Chart.helpers.color('#5D4191').alpha(alpha).darken(0.6).rgbString();
                                },
                                borderWidth: 1,
                                hoverBackgroundColor: 'yellow',
                                hoverBorderColor: 'yellowgreen',
                                width(c) {
                                    const a = c.chart.chartArea || {};
                                    return (a.right - a.left) / 30 - 1;
                                },
                                height(c) {
                                    const a = c.chart.chartArea || {};
                                    return (a.bottom - a.top) / 7.5 - 1;
                                }
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                displayColors: false,
                                callbacks: {
                                    title() {
                                        return '';
                                    },
                                    label(context) {
                                        const v = context.dataset.data[context.dataIndex];
                                        return ['თარიღი: ' + v.d, 'რაოდენობა: ' + v.v.toFixed(2)];
                                    }
                                }
                            }
                            },
                            scales: {
                                x: {
                                    type: 'time',
                                    position: 'bottom',
                                    offset: true,
                                    time: {
                                        unit: 'week',
                                        round: 'week',
                                        isoWeekday: 1,
                                        displayFormats: {
                                            week: 'MMMMMM'
                                        }
                                    },
                                    ticks: {
                                        maxRotation: 0,
                                        autoSkip: true
                                    },
                                    grid: {
                                        display: false,
                                        drawBorder: false,
                                        tickMarkLength: 0,
                                    }
                                },
                                y: {
                                    type: 'time',
                                    offset: true,
                                    time: {
                                        unit: 'day',
                                        round: 'day',
                                        isoWeekday: 1,
                                        parser: 'i',
                                        displayFormats: {
                                            day: 'iiiiii'
                                        }
                                    },
                                    reverse: true,
                                    position: 'right',
                                    ticks: {
                                        maxRotation: 0,
                                        autoSkip: true,
                                        padding: 1
                                    },
                                    grid: {
                                        display: false,
                                        drawBorder: false,
                                        tickMarkLength: 0
                                    }
                                }
                            }
                        }
                    });
                });


    ctx = document.getElementById("monthChart").getContext('2d');
    var monthChart = new Chart(ctx, JSON.parse(data.month_chart));

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
