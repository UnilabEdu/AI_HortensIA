let ctx;

function clone(obj) {
  var result = Array.isArray(obj) ? [] : {};
  for (var key in obj) {
    var value = obj[key];
    var type = {}.toString.call(value).slice(8, -1);
    if (type === 'Array' || type === 'Object') {
      result[key] = clone(value);
    } else if (type === 'Date') {
      result[key] = new Date(value.getTime());
    }  else {
      result[key] = value;
    }
  }
  return result;
}

// CONFIGS

// ["User_wor52", "User_form1363", "User_can1525", "User_302000", "User_cludis32", "User_and957", "User_ar891", "User_and1235", "User_navile849", "User_ther,1251", "YOU \u27a4    "]
// ["rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(127, 92, 194, 1)", "rgba(156, 92, 194, 1)"]
// [3996, 3988, 3984, 3979, 3973, 3955, 3954, 3949, 3944, 3937, 3233]

Chart.overrides.doughnut.cutout = '45%'
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
            maintainAspectRatio: false,
            responsive: true,
            plugins: {
                legend: {
                    display: false,
                }
            }
        }
    }



var bar_ctx = document.getElementById('leaderboardChart').getContext('2d');

const leaderboardNormalGradient = bar_ctx.createLinearGradient(0, 0, 600, 0);
            leaderboardNormalGradient.addColorStop(0, 'purple');
            leaderboardNormalGradient.addColorStop(1, 'rgba(78, 116, 194, 1)');

const leaderboardSpecialGradient = bar_ctx.createLinearGradient(0, 0, 600, 0);
            leaderboardSpecialGradient.addColorStop(0, 'rgba(78, 116, 194, 1)');
            leaderboardSpecialGradient.addColorStop(1, 'purple');

// OLD RED-ORANGE COLORS:
// const leaderboardNormalGradient = bar_ctx.createLinearGradient(0, 0, 1200, 0);
//             leaderboardNormalGradient.addColorStop(0, '#F05B6E');
//             leaderboardNormalGradient.addColorStop(1, '#FCAB5A');
//
// const leaderboardSpecialGradient = bar_ctx.createLinearGradient(0, 0, 400, 0);
//             leaderboardSpecialGradient.addColorStop(0, '#FCAB5A');
//             leaderboardSpecialGradient.addColorStop(1, '#F05B6E');





leaderboardColors = []
for (let count = 0; count < 10; count++) {
    leaderboardColors.push(leaderboardNormalGradient)
}

console.log(leaderboardColors)


const leaderboardChartConfig = {
         type: "bar",
         data: {
             labels: ['', '', '', '', '', '', '', '', '', '', ''],
             datasets: [{
                 label: "Leaderboard",
                 data: [10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5],
                 backgroundColor: leaderboardColors,
                 barThickness: ["flex"],
                 barPercentage: [1],
                 categoryPercentage: [1]
                 }]
         },
        options: {
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
            plugins: {}
        }
        }


const monthChartConfig = {
    type: "line",
    data:
        {labels:
                ['', '', '', ''],
        datasets: [
            {label: "Tickets Filed Last 30 Days",
            data: [4, 2, 3, 1],
            borderColor: 'purple',
            borderWidth: 3,
            backgroundColor: function() {
            var gradient = ctx.createLinearGradient(0, 0, 500, 0);
                gradient.addColorStop(0, 'purple');
                gradient.addColorStop(1, 'rgba(127, 92, 194, 1)');
            return gradient
            },
            tension: 0.4,
            fill: true
            }
            ]
        },
    options:
        {elements:
            {point:
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
                        tickMarkLength: 0}
                        },
                x:
                    {
                    grid:
                        {
                        display: false,
                        drawBorder: false,
                        tickMarkLength: 0}
                        }
                    },
        plugins: {}
        }
    }

const weekChartConfig = clone(monthChartConfig)


const radarAnytimePrimaryConfig = {
    type: "radar",
    data: {
        labels: [
            "Rage", "Vigilance", "Ecstasy", "Admiration", "Terror", "Amazement", "Grief", "Loathing"
        ],
        datasets: [
            {
                label:
                    "My Data",
                data: [1, 1, 1, 1, 1, 1, 1, 1],
                fill: true,
                backgroundColor: "#5200CE13",
                borderColor: "#4E6FCC",
                pointBackgroundColor: "rgba(255, 99, 132, 1)",
                pointBorderColor: "rgba(255, 255, 255, 1)",
                pointHoverBackgroundColor: "rgba(255, 255, 255, 1)",
                pointHoverBorderColor: "rgba(255, 99, 132, 1)",
                tension: 0.1},
            {
                label:
                    "All Data",
                data: [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
                fill: true,
                backgroundColor: "#D014C213",
                borderColor: "#D06FC2",
                pointBackgroundColor: "rgba(54, 162, 235, 1)",
                pointBorderColor: "rgba(255, 255, 255, 1)",
                pointHoverBackgroundColor: "rgba(255, 255, 255, 1)",
                pointHoverBorderColor: "rgba(54, 162, 235, 1)",
                tension: 0.1
            }
        ]
    },
    options: {
        // maintainAspectRatio: false,
        elements:
            {point:
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
        plugins: {}}}

const radarAnytimeSecondaryConfig = clone(radarAnytimePrimaryConfig)
radarAnytimeSecondaryConfig.data.labels = ['Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt']
const streakGoalChartConfig = clone(doughnutChartConfig)
streakGoalChartConfig.data.labels = ['აქტიურობის დღეები', 'დღეები შემდეგ მიზნამდე']
const weeklyGoalChartConfig = clone(doughnutChartConfig)
weeklyGoalChartConfig.data.labels = ['ბოლო 7 დღეს შევსებული ბარათები', 'შევსებული ბარათების სამიზნე რაოდენობა']
const rankupGoalChartConfig = clone(doughnutChartConfig)
rankupGoalChartConfig.data.labels = ['ამდენი ბარათით ასწრებ წინა მომხმარებელს', 'გადასასწრებად დარჩენილი ბარათათები']


// const radarMonthPrimaryConfig = clone(radarAnytimePrimaryConfig)
// const radarMonthSecondaryConfig = clone(radarAnytimeSecondaryConfig)
// const radarWeekPrimaryConfig = clone(radarAnytimePrimaryConfig)
// const radarWeekSecondaryConfig = clone(radarAnytimeSecondaryConfig)
// const radarDayPrimaryConfig = clone(radarAnytimePrimaryConfig)
// const radarDaySecondaryConfig = clone(radarAnytimeSecondaryConfig)

    ctx = document.getElementById("streakGoalChart").getContext('2d');
    var streakGoalChart = new Chart(ctx, streakGoalChartConfig);

    ctx = document.getElementById("weeklyGoalChart").getContext('2d');
    var weeklyGoalChart = new Chart(ctx, weeklyGoalChartConfig);

    ctx = document.getElementById("rankupGoalChart").getContext('2d');
    var rankupGoalChart = new Chart(ctx, rankupGoalChartConfig);



    ctx = document.getElementById("monthChart").getContext('2d');
    var monthChart = new Chart(ctx, monthChartConfig);

    ctx = document.getElementById("weekChart").getContext('2d');
    var weekChart = new Chart(ctx, weekChartConfig);

    ctx = document.getElementById("leaderboardChart").getContext('2d');
    var leaderboardChart = new Chart(ctx, leaderboardChartConfig);

    ctx = document.getElementById("radarChartAnytimePrimary").getContext('2d');
    var radarChartAnytimePrimary = new Chart(ctx, radarAnytimePrimaryConfig)

    ctx = document.getElementById("radarChartAnytimeSecondary").getContext('2d');
    var radarChartAnytimeSecondary = new Chart(ctx, radarAnytimeSecondaryConfig)
    //
    // ctx = document.getElementById("radarChartMonthPrimary").getContext('2d');
    // var radarChartMonthPrimary = new Chart(ctx, radarMonthPrimaryConfig)
    //
    // ctx = document.getElementById("radarChartMonthSecondary").getContext('2d');
    // var radarChartMonthSecondary = new Chart(ctx, radarMonthSecondaryConfig)
    //
    // ctx = document.getElementById("radarChartWeekPrimary").getContext('2d');
    // var radarChartWeekPrimary = new Chart(ctx, radarWeekPrimaryConfig)
    //
    // ctx = document.getElementById("radarChartWeekSecondary").getContext('2d');
    // var radarChartWeekSecondary = new Chart(ctx, radarWeekSecondaryConfig)
    //
    // ctx = document.getElementById("radarChartDayPrimary").getContext('2d');
    // var radarChartDayPrimary = new Chart(ctx, radarDayPrimaryConfig)
    //
    // ctx = document.getElementById("radarChartDaySecondary").getContext('2d');
    // var radarChartDaySecondary = new Chart(ctx, radarDaySecondaryConfig)






















// Generate Empty Heatmap
    		function startOfToday() {
			const d = new Date();
			// TODO: Fix bug and remove console.log
			console.log('DATEHERE:')
            console.log(d)
			return new Date(d.getFullYear(), d.getMonth(), d.getDate(), 0, 0, 0, 0);
		}
		function isoDayOfWeek(dt) {
			let wd = dt.getDay(); // 0..6, from sunday
			wd = (wd + 6) % 7 + 1; // 1..7 from monday
			return '' + wd; // string so it gets parsed
		}

    function generateData() {
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
    		        ctx = document.getElementById('heatmapChart').getContext('2d');
                    heatmapChart = new Chart(ctx, {
                        type: 'matrix',
                        data: {
                            datasets: [{
                                label: 'Activity Heatmap',
                                data: generateData(), // heatmapData
                                // TODO: create a proper formula for choosing colors
                                backgroundColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 0.9;
                                    const alpha = (10 + value) / 60;
                                    return Chart.helpers.color('#7E57C2').alpha(alpha).lighten(0.1 / c.dataset.data[c.dataIndex].v).rgbString();
                                },
                                borderColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 0.9;
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

// End of Generate Empty Heatmap
