// chart-configs.js initializes every chart on the dashboard, applies necessary styles and default values


function clone(obj) { // Used only to clone chart configs
    let result = Array.isArray(obj) ? [] : {};
    for (let key in obj) {
        let value = obj[key];
        let type = {}.toString.call(value).slice(8, -1);
        if (type === 'Array' || type === 'Object') {
            result[key] = clone(value);
        } else if (type === 'Date') {
            result[key] = new Date(value.getTime());
        } else {
            result[key] = value;
        }
    }
    return result;
}

// Global settings for Chart.js
Chart.defaults.font.family = "'FiraGO', 'BPG Nino Mtavruli', sans-serif"
Chart.overrides.doughnut.cutout = '45%'




// Chart config used for every Donut chart
const doughnutChartConfig = {
    type: "doughnut",
    data: {
        labels: [
            '',
            '',
        ],
        datasets: [{
            data: [7, 0],
            backgroundColor: [
                '#914EB2',
                '#FCF3FE',
            ],
            hoverOffset: 0
        }]
    },
    options: {
        elements: {
            arc: {
                borderWidth: 0
            }
        },
        maintainAspectRatio: false,
        responsive: true,
        plugins: {
            legend: {
                display: false,
            }
        }
    }
}

// Initializing gradients to be used in leaderboard chart and streaks chart
const bar_ctx = document.getElementById('leaderboardChart').getContext('2d');

const leaderboardNormalGradient = bar_ctx.createLinearGradient(0, 0, 400, 0);
leaderboardNormalGradient.addColorStop(0, 'rgba(159,13,180,0.8)');
leaderboardNormalGradient.addColorStop(1, 'rgba(243,77,94,0.8)');

const leaderboardSpecialGradient = bar_ctx.createLinearGradient(0, 0, 400, 0);
leaderboardSpecialGradient.addColorStop(0, 'rgba(243,77,94,0.8)');
leaderboardSpecialGradient.addColorStop(1, 'rgba(159,13,180,0.8)');

leaderboardColors = []
for (let count = 0; count < 10; count++) {
    leaderboardColors.push(leaderboardNormalGradient)
}




// A bar chart config used for leaderboard chart and streaks chart
const leaderboardChartConfig = {
    type: "bar",
    data: {
        labels: ['', '', '', '', '', '', '', '', '', '', ''],
        datasets: [{
            label: "Leaderboard",
            data: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            backgroundColor: leaderboardColors,
            barThickness: ["flex"],
            barPercentage: [1],
            categoryPercentage: [1]
        }]
    },
    options: {
        elements:
        {
            point:
                {
                    radius: 5,
                    hoverRadius: 20
                }
        },
        maintainAspectRatio: false,
        indexAxis: "y",
        scales: {
            y: {
                ticks: {
                    crossAlign: 'far',
                },
                grid: {
                    "display": false,
                    "drawBorder": false,
                    "tickMarkLength": 0
                }
            },
            x: {
                grid: {
                    display: false,
                    drawBorder: false,
                    tickMarkLength: 0
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
}



// Chart config for the last month's activity line chart
const monthChartConfig = {
    type: "line",
    data:
        {
            labels:
                ['', '', '', ''],
            datasets: [
                {
                    label: txt.dash.act.line.month,
                    data: [4, 2, 3, 1],
                    borderColor: '#8f1993',
                    borderWidth: 3,
                    backgroundColor: function () {
                        let gradient = ctx.createLinearGradient(0, 0, 600, 0);
                        gradient.addColorStop(0, '#791993');
                        gradient.addColorStop(1, 'rgb(236,93,105)');
                        return gradient
                    },
                    tension: 0.4,
                    fill: true
                }
            ]
        },
    options:
        {
            elements:
                {
                    point:
                        {
                            radius: 0,
                            hitRadius: 25
                        }
                },
            scales:
                {
                    y:
                        {
                            beginAtZero: true,
                            grid:
                                {
                                    display: false,
                                    drawBorder: false,
                                    tickMarkLength: 0
                                }
                        },
                    x:
                        {
                            grid:
                                {
                                    display: false,
                                    drawBorder: false,
                                    tickMarkLength: 0
                                }
                        }
                },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
}




// Radar chart config used in the primary and secondary radar charts
const radarAnytimePrimaryConfig = {
    type: "radar",
    data: {
        labels: txt.dash.radar.primary.emotions,
        datasets: [
            {
                label: txt.dash.radar.labels.my,
                data: [1, 1, 1, 1, 1, 1, 1, 1],
                fill: true,
                backgroundColor: "#5200CE13",
                borderColor: "#4E6FCC",
                pointBackgroundColor: "#4E6FCC",
                pointBorderColor: "#5200CE",
                pointHoverBackgroundColor: "#4E6FCC",
                pointHoverBorderColor: "#5200CE",
                tension: 0.3
            },
            {
                label: txt.dash.radar.labels.all,
                data: [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
                fill: true,
                backgroundColor: "#D014C213",
                borderColor: "#D06FC2",
                pointBackgroundColor: "#D014C2",
                pointBorderColor: "#D06FC2",
                pointHoverBackgroundColor: "#D014C2",
                pointHoverBorderColor: "#D06FC2",
                tension: 0.3
            }
        ]
    },
    options: {
        responsive: true,
        elements:
            {
                point:
                    {
                        radius: 0,
                        hitRadius: 50
                    }
            },
        scales: {
            r: {
                pointLabels: {
                    font: {
                        size: 18,
                        family: 'sans-serif'
                    }
                },
                beginAtZero: true,
                grid: {
                    display: false
                }
            }
        },
        plugins: {
            legend: {
                labels: {
                    font: {
                        family: "'FiraGO', 'BPG Nino Mtavruli', sans-serif"
                    }
                }
            }
        }
    }
}

// Clone all of the Chart Configs to appropriate constants. Change labels and other text info where necessary

// All Donut charts (Goal charts)
const streakGoalChartConfig = clone(doughnutChartConfig)
streakGoalChartConfig.data.labels = txt.dash.goal.streak.tooltips
const weeklyGoalChartConfig = clone(doughnutChartConfig)
weeklyGoalChartConfig.data.labels = txt.dash.goal.lvl.tooltips
const rankupGoalChartConfig = clone(doughnutChartConfig)
rankupGoalChartConfig.data.labels = txt.dash.goal.rank.tooltips

// Streaks chart is the same as Leaderboard chart
const topStreaksChartConfig = clone(leaderboardChartConfig)
topStreaksChartConfig.data.datasets[0].label = txt.dash.lead.streaks.title

// Secondary Radar chart is the same as Primary Radar
const radarAnytimeSecondaryConfig = clone(radarAnytimePrimaryConfig)
radarAnytimeSecondaryConfig.data.labels = txt.dash.radar.secondary.emotions


// Create charts based on configs

// Goal charts
ctx = document.getElementById("streakGoalChart").getContext('2d');
const streakGoalChart = new Chart(ctx, streakGoalChartConfig);

ctx = document.getElementById("weeklyGoalChart").getContext('2d');
const weeklyGoalChart = new Chart(ctx, weeklyGoalChartConfig);

ctx = document.getElementById("rankupGoalChart").getContext('2d');
const rankupGoalChart = new Chart(ctx, rankupGoalChartConfig);

// Activity chart
ctx = document.getElementById("monthChart").getContext('2d');
const monthChart = new Chart(ctx, monthChartConfig);

// Top-10 charts (leaderboard and streaks)
ctx = document.getElementById("leaderboardChart").getContext('2d');
const leaderboardChart = new Chart(ctx, leaderboardChartConfig);

ctx = document.getElementById("topStreaksChart").getContext('2d');
const topStreaksChart = new Chart(ctx, topStreaksChartConfig);

// Radar charts
ctx = document.getElementById("radarChartAnytimePrimary").getContext('2d');
const radarChartAnytimePrimary = new Chart(ctx, radarAnytimePrimaryConfig)

ctx = document.getElementById("radarChartAnytimeSecondary").getContext('2d');
const radarChartAnytimeSecondary = new Chart(ctx, radarAnytimeSecondaryConfig)




// Generate Empty Heatmap

// Initialize functions needed to generate a heatmap
function startOfToday() {
    const d = new Date();
    return new Date(d.getFullYear(), d.getMonth(), d.getDate(), 0, 0, 0, 0);
}

function isoDayOfWeek(dt) {
    let wd = dt.getDay(); // 0..6, from sunday
    wd = (wd + 6) % 7 + 1; // 1..7 from monday
    return '' + wd; // string so it gets parsed
}

function generateData() { // Generates data for an empty heatmap with 182 days
    const data = [];
    const end = startOfToday();
    let dt = new Date(new Date().setDate(end.getDate() - 182));
    while (dt <= end) {
        const iso = dt.toISOString().substr(0, 10);
        data.push({
            x: iso,
            y: isoDayOfWeek(dt),
            d: iso,
            v: 0
        });
        dt = new Date(dt.setDate(dt.getDate() + 1));
    }
    return data;
}


Chart.defaults.fontSize = 9;
let heatmapColorHelper = [0, 1]


// Create a Heatmap
ctx = document.getElementById('heatmapChart').getContext('2d');
heatmapChart = new Chart(ctx, {
    type: 'matrix',
    data: {
        datasets: [{
            label: 'Activity Heatmap',
            data: generateData(), // heatmapData
            backgroundColor(c) {
                const value = c.dataset.data[c.dataIndex].v - heatmapColorHelper[0] / (heatmapColorHelper[1] - heatmapColorHelper[0]);
                const alpha = (value) / 30;
                return Chart.helpers.color('#791993').alpha(alpha).lighten(0.1 / c.dataset.data[c.dataIndex].v).rgbString();
            },
            borderColor(c) {
                const value = c.dataset.data[c.dataIndex].v - heatmapColorHelper[0] / (heatmapColorHelper[1] - heatmapColorHelper[0]);
                const alpha = (10 + value * 10) / 60;
                return Chart.helpers.color('#4c0e5c').alpha(alpha).darken(0.6).rgbString();
            },
            borderWidth: 1.1,
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
                        return [txt.dash.act.heatmap.date + ': ' + v.d, txt.dash.act.heatmap.amount + ': ' + v.v.toFixed(2)];
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
