from flask import render_template
from .generate_charts import generate_charts
from . import dashboard_blueprint
import json


# TODO: @login_required
@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    ChartMonth, ChartWeek, ChartLeaderboard, ChartRadar, heatmap_data = generate_charts()
    MonthChart = ChartMonth()
    month_chart = MonthChart.get()

    WeekChart = ChartWeek()
    week_chart = WeekChart.get()

    LeaderboardChart = ChartLeaderboard()
    leaderboard_chart = LeaderboardChart.get()

    RadarChart = ChartRadar()
    radar_chart = RadarChart.get()

    heatmap_json = json.dumps(heatmap_data)

    return render_template('dashboard.html', week_chart=week_chart, month_chart=month_chart,
                           leaderboard_chart=leaderboard_chart, heatmap_json=heatmap_json,
                           radar_chart=radar_chart)
