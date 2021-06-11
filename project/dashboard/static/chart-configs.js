// Generate Empty Heatmap
    		function startOfToday() {
			const d = new Date();
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
                    let ctx = document.getElementById('heatmapChart').getContext('2d');
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
