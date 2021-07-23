function showChart(chartName, chartGroup, button, additionalDiv = 0) {
    var i;
    let x;
    if (chartGroup === 'activity') {
        x = document.getElementsByClassName("activity-chart-container");
    } else if (chartGroup === 'leaderboards') {
        x = document.getElementsByClassName("leaderboard-chart-container");
    }
    for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
    }
    document.getElementById(chartName).style.display = "block";

    if (additionalDiv !== 0) {
        document.getElementById(additionalDiv).style.display = "block"
    }

    let allButtons;
    console.log(button.classList)
    if (button.classList.contains('statistics__buttonsActivity')) {
        console.log('activity')
        allButtons = document.querySelectorAll('.statistics__buttonsActivity')
        console.log('allButtons')
        console.log(allButtons)
    } else if (button.classList.contains('statistics__buttonsLeaderboards')) {
        console.log('leaderboard')
        allButtons = document.querySelectorAll('.statistics__buttonsLeaderboards')
    }

    for (let i = 0; i < allButtons.length; i++) {
        if (allButtons[i].classList.contains('statistics__active')) {
            console.log('contains')
            allButtons[i].classList.remove('statistics__active')
        }
    }
    button.classList.add('statistics__active')
}




function updateChartData(chart, label, data, infoLabel=null) {
    chart.data.labels = label
    chart.data.datasets.forEach((dataset) => {
        dataset.data = data;
        if (infoLabel) {
            dataset.label = infoLabel
        }
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

function activateRadarButtons(btn) {
    let allRadarButtons = document.querySelectorAll('.statistics__buttonsRadars button')
    for (let i = 0; i < allRadarButtons.length; i++) {
        console.log(btn.classList)
        if (allRadarButtons[i].classList.contains('statistics__active')) {
            allRadarButtons[i].classList.remove('statistics__active')
        }
    }
    btn.classList.add('statistics__active')
}


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
    chart.update();
}


function updateRankupChart(chart, data) {
    if (data[1] === 'leader') {
        chart.data.datasets[0].data = [data[0], 0]
        document.getElementById("rankup-text").innerHTML = txt.dash.goal.rank.top.info
        document.getElementById("rankup-goal").innerHTML = txt.dash.goal.rank.top.targ
        chart.data.datasets[0].backgroundColor = ['#2E9877']
        chart.update()
    } else if (data[1] > 0) {
        if (data[0] === 0) {
            data[0] = 0.1
        }
        chart.data.datasets[0].data = data;
        chart.update()
        document.getElementById("rankup-text").innerHTML = txt.dash.goal.rank.calculated.info
        document.getElementById("rankup-goal").innerHTML = txt.dash.goal.rank.calculated.targ[0] + data[1].toString() + txt.dash.goal.rank.calculated.targ[1];

    } else {
        document.getElementById("rankup-text").innerHTML = txt.dash.goal.rank.default.info
        document.getElementById("rankup-goal").innerHTML = txt.dash.goal.rank.default.targ
    }
}

function updateStreakGoalChart(chart, streakDays) {
    var colors = ['#914EB2', '#916DD1', '#4B6DD1', '#0098BD', '#00CEBD', '#F7B967', '#F78C67', '#FF5050', '#F74991', '#00C4E3', '#DE2A7C']
    var brackets = [7, 14, 21, 30, 60, 90, 120, 150, 180, 365, 99999999]
    let currentBracket = 7
    let bracketIndex = 0
    let activeStreak = true
    if (streakDays < 0) {
        streakDays = Math.abs(streakDays)
        activeStreak = false
    }


    brackets.forEach(function(value, index, array) {

        if (streakDays >= value) {
            currentBracket = array[index+1]
            bracketIndex = index + 1
        }
    })

    var currentStreakText;
    var targetStreakText;
    if (activeStreak === true) {
        currentStreakText = txt.dash.goal.streak.calculated.active.curr[0] + streakDays.toString() + txt.dash.goal.streak.calculated.active.curr[1]

        if (streakDays === 0) {
            currentStreakText = txt.dash.goal.streak.default.curr
            targetStreakText = txt.dash.goal.streak.default.targ
            chart.data.datasets[0].backgroundColor[1] = '#E5D4F0'
        } else if (bracketIndex === 10) {
            targetStreakText = txt.dash.goal.streak.calculated.active.targ.end
        } else if (bracketIndex === 9) {
            targetStreakText = txt.dash.goal.streak.calculated.active.targ.year
        } else if (bracketIndex > 2) {
            targetStreakText = txt.dash.goal.streak.calculated.active.targ.month[0] + (bracketIndex - 2).toString() + txt.dash.goal.streak.calculated.active.targ.month[1]
        } else {
            targetStreakText = txt.dash.goal.streak.calculated.active.targ.week[0] + (bracketIndex + 1).toString() + txt.dash.goal.streak.calculated.active.targ.week[1]
        }
    } else {
        currentStreakText = txt.dash.goal.streak.calculated.paused.curr[0] + streakDays.toString() + txt.dash.goal.streak.calculated.paused.curr[1]
        targetStreakText = txt.dash.goal.streak.calculated.paused.targ
    }

    let values;

    values = [streakDays, currentBracket - streakDays]

    document.getElementById("current-streak-text").innerHTML = currentStreakText;
    document.getElementById("target-streak-text").innerHTML = targetStreakText;

    chart.data.datasets[0].data = values;
    chart.data.datasets[0].backgroundColor[0] = colors[bracketIndex]

    chart.update();
}


function updateWeeklyGoalChart(chart, weekData) {
    let levelGoals = [35, 70, 105]

    let weekDataSum = weekData.reduce(function (a, b) {
        return a + b;
    }, 0);

    document.getElementById("weekly-goal-text").innerHTML = txt.dash.goal.lvl.curr[0] + weekDataSum.toString() + txt.dash.goal.lvl.curr[1];

    let goalText;
    let targetAmount;
    if (weekDataSum >= levelGoals[2]) {
        targetAmount = 0
        goalText = txt.dash.goal.lvl.targ[3]
    } else if (weekDataSum >= levelGoals[1]) {
        targetAmount = levelGoals[2] - weekDataSum
        goalText = txt.dash.goal.lvl.targ[2][0] + targetAmount.toString() + txt.dash.goal.lvl.targ[2][1]
    } else if (weekDataSum >= levelGoals[0]) {
        targetAmount = levelGoals[1] - weekDataSum
        goalText = txt.dash.goal.lvl.targ[1][0] + targetAmount.toString() + txt.dash.goal.lvl.targ[0][1]
    } else {
        targetAmount = levelGoals[0] - weekDataSum
        goalText = txt.dash.goal.lvl.targ[0][0] + targetAmount.toString() + txt.dash.goal.lvl.targ[0][1]
    }
    document.getElementById("weekly-goal-stage").innerHTML = goalText

    chart.data.datasets[0].data = [weekDataSum, targetAmount];
    chart.update()
}


function updateWeeklyLevelsTable(tableID, displayLevel, button) {
    let table = document.getElementById(tableID)
    let tbody = table.getElementsByTagName('tbody')[0];

    let data = weeklyLevelsData

    if (weeklyTableCurrentLevel !== displayLevel) {
        // clear table
        while (table.rows.length > 1) {
            table.deleteRow(1)
        }

        if (displayLevel === 1) {
            if (data.level_one.length > 0) {
                levelData = data.level_one
            } else {
                levelData = [txt.dash.lead.levels.one]
            }
            weeklyTableCurrentLevel = 1
            table.className = 'table__green'

        } else if (displayLevel === 2) {
            if (data.level_two.length > 0) {
                levelData = data.level_two
            } else {
                levelData = [txt.dash.lead.levels.two]
            }
            weeklyTableCurrentLevel = 2
            table.className = 'table__blue'

        } else if (displayLevel === 3) {
            if (data.level_three.length > 0) {
                levelData = data.level_three
            } else {
                levelData = [txt.dash.lead.levels.three]

            }
            weeklyTableCurrentLevel = 3
            table.className = 'table__red'

        }

        let rowsToAppend = []
        for (let i = 0; i < levelData.length; i++) {
            let row = document.createElement('tr')
            var cellUsername = document.createElement("td");
            var cellFrequency = document.createElement("td");
            var cellUsernameText = document.createTextNode(levelData[i][0]);
            var cellFrequencyText = document.createTextNode(levelData[i][1].toString())
            cellUsername.appendChild(cellUsernameText)
            cellFrequency.appendChild(cellFrequencyText)
            row.appendChild(cellUsername)
            row.appendChild(cellFrequency)
            rowsToAppend.push(row)
        }

        for (let i = 0; i < rowsToAppend.length; i++) {
            tbody.appendChild(rowsToAppend[i])
        }

        let allButtons = document.querySelectorAll('.statistics__buttonsTableLevels')
        for (let i = 0; i < allButtons.length; i++) {
            if (allButtons[i].classList.contains('statistics__active')) {
                allButtons[i].classList.remove('statistics__active')
            }
            button.classList.add('statistics__active')
        }
    }
}







var fetchActivityData = async function () {
    var response = await fetch('/dashboard/getactivitydata');
    return await response.json()
};

async function renderActivityCharts() {
    activityData = await fetchActivityData();
    let heatmapData = activityData.heatmap_data
    let monthLabels = activityData.month_chart_labels
    let monthData = activityData.month_chart_frequencies
    let weekLabels = activityData.month_chart_labels.slice(-7)
    let weekData = activityData.month_chart_frequencies.slice(-7)
    let streakData = activityData.streak
    updateHeatmap(heatmapChart, heatmapData)
    updateChartData(monthChart, monthLabels, monthData);
    updateWeeklyGoalChart(weeklyGoalChart, weekData)
    updateStreakGoalChart(streakGoalChart, streakData)

    heatmapColorHelper = activityData.min_max


    var buttonWeek = document.getElementById('btn-activity-chart-week')
    var buttonMonth = document.getElementById('btn-activity-chart-month')


    buttonWeek.addEventListener("click", function () {
                updateChartData(monthChart, weekLabels, weekData)
                console.log(buttonMonth.classList)
                if (buttonMonth.classList.contains('statistics__active')) {
                    buttonMonth.classList.remove('statistics__active')
                }
                buttonWeek.classList.add('statistics__active')
    })

    buttonMonth.addEventListener("click", function () {
                updateChartData(monthChart, monthLabels, monthData)
                if (buttonWeek.classList.contains('statistics__active')) {
                    buttonWeek.classList.remove('statistics__active')
                }
                buttonMonth.classList.add('statistics__active')
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
        activateRadarButtons(buttonAnytime)
    })

    buttonMonth.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_month_primary, data.everyone_month_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_month_secondary, data.everyone_month_secondary])
        activateRadarButtons(buttonMonth)
    })

    buttonWeek.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_week_primary, data.everyone_week_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_week_secondary, data.everyone_week_secondary])
        activateRadarButtons(buttonWeek)
    })

    buttonDay.addEventListener("click", function () {
        updateRadar(radarChartAnytimePrimary, [data.user_day_primary, data.everyone_day_primary])
        updateRadar(radarChartAnytimeSecondary, [data.user_day_secondary, data.everyone_day_secondary])
        activateRadarButtons(buttonDay)
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
    let rankUpData = fetchedData.rank_up_data
    updateChartData(leaderboardChart, leaderboardLabels, leaderboardData)
    updateLeaderboardColors(leaderboardChart, userRank)
    updateRankupChart(rankupGoalChart, rankUpData)
}

renderLeaderboardChart()



var fetchWeeklyLevelsData = async function () {
    var response = await fetch('/dashboard/getweeklylevelsdata');
    return await response.json();
};

async function renderWeeklyLevelsTable() {
    weeklyLevelsData = await fetchWeeklyLevelsData();
    weeklyTableCurrentLevel = 0
    updateWeeklyLevelsTable('table-leaderboards-weekly', 1, document.querySelector('.statistics__buttonsTableLevels'))
}

renderWeeklyLevelsTable()



var fetchTopStreaksData = async function () {
    var response = await fetch('/dashboard/gettopstreaksdata');
    return await response.json();
};

async function renderTopStreaksChart() {
    streaksData = await fetchTopStreaksData();
    var usernames = streaksData.usernames
    var scores = streaksData.top_streaks
    updateChartData(topStreaksChart, usernames, scores)
}

renderTopStreaksChart()
