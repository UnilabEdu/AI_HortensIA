from flask import render_template, make_response, jsonify
from .generate_charts import generate_charts, generate_radars
from .data_processing import data_user_activity, data_leaderboard, data_radar
from . import dashboard_blueprint
import json


# TODO: @login_required
@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html',)


@dashboard_blueprint.route('/testme')
def testme():
    # ChartMonth, ChartWeek, ChartLeaderboard, heatmap_data = generate_charts()
    #
    # MonthChart = ChartMonth()
    # month_chart = MonthChart.get()
    #
    # WeekChart = ChartWeek()
    # week_chart = WeekChart.get()
    #
    # LeaderboardChart = ChartLeaderboard()
    # leaderboard_chart = LeaderboardChart.get()
    #
    # heatmap_json = json.dumps(heatmap_data)
    #
    # primary_anytime, secondary_anytime, primary_month, secondary_month, \
    # primary_week, secondary_week, primary_day, secondary_day = generate_radars()
    #
    # # Radar Charts
    # ChartPrimaryAnytime = primary_anytime()
    # primary_anytime_chart = ChartPrimaryAnytime.get()
    # ChartSecondaryAnytime = secondary_anytime()
    # secondary_anytime_chart = ChartSecondaryAnytime.get()
    #
    # ChartPrimaryMonth = primary_month()
    # primary_month_chart = ChartPrimaryMonth.get()
    # ChartSecondaryMonth = secondary_month()
    # secondary_month_chart = ChartSecondaryMonth.get()
    #
    # ChartPrimaryWeek = primary_week()
    # primary_week_chart = ChartPrimaryWeek.get()
    # ChartSecondaryWeek = secondary_week()
    # secondary_week_chart = ChartSecondaryWeek.get()
    #
    # ChartPrimaryDay = primary_day()
    # primary_day_chart = ChartPrimaryDay.get()
    # ChartSecondaryDay = secondary_day()
    # secondary_day_chart = ChartSecondaryDay.get()
    # print(secondary_day_chart)
    #
    # return render_template('radars.html', week_chart=week_chart, month_chart=month_chart,
    #                        leaderboard_chart=leaderboard_chart, heatmap_json=heatmap_json,
    #                        primary_anytime_chart=primary_anytime_chart, secondary_anytime_chart=secondary_anytime_chart,
    #                        primary_month_chart=primary_month_chart, secondary_month_chart=secondary_month_chart,
    #                        primary_week_chart=primary_week_chart, secondary_week_chart=secondary_week_chart,
    #                        primary_day_chart=primary_day_chart, secondary_day_chart=secondary_day_chart)
    return render_template('test.html')


# TODO: use flask-limit on fetching routes
@dashboard_blueprint.route('/getradarsdata')
def get_radars_data():
    primary, secondary = data_radar()
    everyone_anytime_primary, everyone_month_primary, everyone_week_primary, everyone_day_primary = primary[0:4]
    user_anytime_primary, user_month_primary, user_week_primary, user_day_primary = primary[4:9]

    everyone_anytime_secondary, everyone_month_secondary, everyone_week_secondary, everyone_day_secondary = secondary[
                                                                                                            0:4]
    user_anytime_secondary, user_month_secondary, user_week_secondary, user_day_secondary = secondary[4:9]

    all_radar_chart_data = dict(everyone_anytime_primary=everyone_anytime_primary,
                                everyone_month_primary=everyone_month_primary,
                                everyone_week_primary=everyone_week_primary,
                                everyone_day_primary=everyone_day_primary,
                                user_anytime_primary=user_anytime_primary,
                                user_month_primary=user_month_primary,
                                user_week_primary=user_week_primary,
                                user_day_primary=user_day_primary,
                                everyone_anytime_secondary=everyone_anytime_secondary,
                                everyone_month_secondary=everyone_month_secondary,
                                everyone_week_secondary=everyone_week_secondary,
                                everyone_day_secondary=everyone_day_secondary,
                                user_anytime_secondary=user_anytime_secondary,
                                user_month_secondary=user_month_secondary,
                                user_week_secondary=user_week_secondary,
                                user_day_secondary=user_day_secondary)

    return make_response(jsonify(all_radar_chart_data))


@dashboard_blueprint.route('/getactivitydata')
def get_activity_data():
    data_month_frequencies, data_month_labels, heatmap_data, streak = data_user_activity()

    month_chart_labels = data_month_labels
    month_chart_frequencies = data_month_frequencies

    # print('____________________WEEK CHART:\n', week_chart, '\n\n\n')
    # print('____________________MONTH CHART:\n', month_chart, '\n\n\n')
    # print('____________________LEADERBOARD CHART:\n', leaderboard_chart, '\n\n\n')
    # print('____________________HEATMAP DATA:\n', heatmap_data, '\n\n\n')

    # print('MONTH_CHART_LABELS:\n', month_chart_labels)
    # print('MONTH_CHART_DATA:\n', month_chart_frequencies)

    all_activity_chart_data = dict(month_chart_labels=month_chart_labels,
                                   month_chart_frequencies=month_chart_frequencies,
                                   heatmap_data=heatmap_data,
                                   streak=streak)

    return make_response(jsonify(all_activity_chart_data))


@dashboard_blueprint.route('/getleaderboarddata')
def get_leaderboard_data():
    leaderboard_labels, leaderboard_data, current_user_rank = data_leaderboard()

    all_leaderboard_data = dict(leaderboard_labels=leaderboard_labels,
                                leaderboard_data=leaderboard_data,
                                current_user_rank=current_user_rank)

    return make_response(jsonify(all_leaderboard_data))
