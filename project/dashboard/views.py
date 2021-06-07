from flask import render_template
from .generate_charts import generate_charts, generate_radars
from . import dashboard_blueprint
import json


# TODO: @login_required
@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    ChartMonth, ChartWeek, ChartLeaderboard, heatmap_data = generate_charts()

    MonthChart = ChartMonth()
    month_chart = MonthChart.get()

    WeekChart = ChartWeek()
    week_chart = WeekChart.get()

    LeaderboardChart = ChartLeaderboard()
    leaderboard_chart = LeaderboardChart.get()

    heatmap_json = json.dumps(heatmap_data)

    primary_anytime, secondary_anytime, primary_month, secondary_month, \
    primary_week, secondary_week, primary_day, secondary_day = generate_radars()

    # Radar Charts
    ChartPrimaryAnytime = primary_anytime()
    primary_anytime_chart = ChartPrimaryAnytime.get()
    ChartSecondaryAnytime = secondary_anytime()
    secondary_anytime_chart = ChartSecondaryAnytime.get()

    ChartPrimaryMonth = primary_month()
    primary_month_chart = ChartPrimaryMonth.get()
    ChartSecondaryMonth = secondary_month()
    secondary_month_chart = ChartSecondaryMonth.get()

    ChartPrimaryWeek = primary_week()
    primary_week_chart = ChartPrimaryWeek.get()
    ChartSecondaryWeek = secondary_week()
    secondary_week_chart = ChartSecondaryWeek.get()

    ChartPrimaryDay = primary_day()
    primary_day_chart = ChartPrimaryDay.get()
    ChartSecondaryDay = secondary_day()
    secondary_day_chart = ChartSecondaryDay.get()

    return render_template('radars.html', week_chart=week_chart, month_chart=month_chart,
                           leaderboard_chart=leaderboard_chart, heatmap_json=heatmap_json,
                           primary_anytime_chart=primary_anytime_chart, secondary_anytime_chart=secondary_anytime_chart,
                           primary_month_chart=primary_month_chart, secondary_month_chart=secondary_month_chart,
                           primary_week_chart=primary_week_chart, secondary_week_chart=secondary_week_chart,
                           primary_day_chart=primary_day_chart, secondary_day_chart=secondary_day_chart)
