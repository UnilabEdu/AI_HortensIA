function showChart(chartName, chartGroup, additionalDiv = 0) {
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
}




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
    chart.update();
}


function updateRankupChart(chart, data) {
    if (data[1] > 0) {
        if (data[0] === 0) {
            data[0] = 0.1
        }
        chart.data.datasets[0].data = data;
        chart.update()
        document.getElementById("rankup-text").innerHTML = 'გადაასწარი ლიდერბორდში შემდეგ მომხმარებელს'
        document.getElementById("rankup-goal").innerHTML = 'შეავსე კიდევ ' + data[1].toString() + ' ბარათი.';

    } else {
        document.getElementById("rankup-text").innerHTML = 'აქ დაგითვლით ლიდერბორდში გადასასწრებად დარჩენილი ბარათების რაოდენობას';
        document.getElementById("rankup-goal").innerHTML = 'დაიწყე ბარათების შევსება';
    }
}

function updateStreakGoalChart(chart, streakDays) {
    var colors = ['#914EB2', '#916DD1', '#4B6DD1', '#0098BD', '#00CEBD', '#F7B967', '#F78C67', '#FF5050', '#F74991', '#00C4E3', '#DE2A7C']
    var brackets = [7, 14, 21, 30, 60, 90, 120, 150, 180, 360, 99999999]
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
        currentStreakText = 'ზედიზედ ' + streakDays.toString() + ' დღე აქტიურობ.'

        if (streakDays === 0) {
            currentStreakText = 'დღეს ბარათი არ შეგივსია.'
            targetStreakText = 'აქ დაგითვლით, ზედიზედ რამდენი დღე იაქტიურე.'
            chart.data.datasets[0].backgroundColor[1] = '#E5D4F0'
        } else if (bracketIndex === 10) {
            targetStreakText = 'დიდი მადლობა!'
        } else if (bracketIndex === 9) {
            targetStreakText = 'შემდეგი მიზანი: 1 წელი.'
        } else if (bracketIndex > 2) {
            targetStreakText = 'შემდეგი მიზანი: ' + (bracketIndex - 2).toString() + ' თვე.'
        } else {
            targetStreakText = 'შემდეგი მიზანი: ' + (bracketIndex + 1).toString() + ' კვირა.'
        }
    } else {
        currentStreakText = 'ზედიზედ ' + streakDays.toString() + ' დღე აქტიურობდი.'
        targetStreakText = 'შეავსე ბარათი დღესაც, რათა გააგრძელო აქტიურობის მიმდევრობა'
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

    document.getElementById("weekly-goal-text").innerHTML = "ბოლო 7 დღეში შეავსე " + weekDataSum.toString() + " ბარათი.";

    let goalText;
    let targetAmount;
    if (weekDataSum >= levelGoals[2]) {
        targetAmount = 0
        goalText = "მესამე დონის კონტრიბუტორი ხარ. დიდი მადლობა!"
    } else if (weekDataSum >= levelGoals[1]) {
        targetAmount = levelGoals[2] - weekDataSum
        goalText = "მესამე დონეზე გადასასვლელად შეავსე კიდევ " + targetAmount.toString() + " ბარათი"
    } else if (weekDataSum >= levelGoals[0]) {
        targetAmount = levelGoals[1] - weekDataSum
        goalText = "მეორე დონეზე გადასასვლელად შეავსე კიდევ " + targetAmount.toString() + " ბარათი"
    } else {
        targetAmount = levelGoals[0] - weekDataSum
        goalText = "პირველ დონეზე გადასასვლელად შეავსე კიდევ " + targetAmount.toString() + " ბარათი"
    }
    document.getElementById("weekly-goal-stage").innerHTML = goalText

    chart.data.datasets[0].data = [weekDataSum, targetAmount];
    chart.update()
}


function updateWeeklyLevelsTable(tableID, displayLevel) {
    let table = document.getElementById(tableID)
    let tbody = table.getElementsByTagName('tbody')[0];

    let data = weeklyLevelsData

    if (weeklyTableCurrentLevel !== displayLevel) {
        // clear table
        while (table.rows.length > 1) {
            table.deleteRow(1)
        }

        if (displayLevel === 1) {
            levelData = data.level_one
            console.log(levelData)
            weeklyTableCurrentLevel = 1
        } else if (displayLevel === 2) {
            levelData = data.level_two
            weeklyTableCurrentLevel = 2
        } else if (displayLevel === 3) {
            levelData = data.level_three
            weeklyTableCurrentLevel = 3
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
    }
}







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
        let streakData = activityData.streak
        updateHeatmap(heatmapChart, heatmapData)
        updateChartData(monthChart, monthLabels, monthData);
        updateChartData(weekChart, weekLabels, weekData)
        updateWeeklyGoalChart(weeklyGoalChart, weekData)
        updateStreakGoalChart(streakGoalChart, streakData)


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
    updateWeeklyLevelsTable('table-leaderboards-weekly', 1)
}

renderWeeklyLevelsTable()
