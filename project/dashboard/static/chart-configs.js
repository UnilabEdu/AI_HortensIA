let ctx;

function clone(obj) {
  var result = Array.isArray(obj) ? [] : {};
  for (var key in obj) {
    // include prototype properties
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
const leaderboardChartConfig = {
         type: "bar",
         data: {
             labels: ['', '', '', '', '', '', '', '', '', '', ''],
             datasets: [{
                 label: "Leaderboard",
                 data: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.5],
                 backgroundColor: 'red',
                 barThickness: ["flex"],
                 barPercentage: [1],
                 categoryPercentage: [1]
                 }]
         },
        options: {
             indexAxis: "y",
             scales: {
                 y: {
                     "grid": {
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
            borderColor: function() {
        var gradient = ctx.createLinearGradient(0, 0, 500, 0);
        gradient.addColorStop(0, 'orange');
        gradient.addColorStop(1, 'purple');
        return gradient
        },
            borderWidth: 2,
            backgroundColor: "rgba(127, 92, 194, 1)",
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
        elements:
            {point:
                    {
                    radius: 0,
                    hitRadius: 50
                    }
            },
        scales: {
            r: {
                beginAtZero: true,
                grid: {
                    display: false
                }
            }
            },
        plugins: {}}}

const radarAnytimeSecondaryConfig = clone(radarAnytimePrimaryConfig)
radarAnytimeSecondaryConfig.data.labels = ['Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt']




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
                                backgroundColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 1.15;
                                    const alpha = (10 + value) / 60;
                                    return Chart.helpers.color('#7E57C2').alpha(alpha).lighten(0.1 / c.dataset.data[c.dataIndex].v).rgbString();
                                },
                                borderColor(c) {
                                    const value = c.dataset.data[c.dataIndex].v * 1.15;
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
