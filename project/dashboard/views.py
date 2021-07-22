from flask import render_template, make_response, jsonify
from .generate_charts import generate_charts, generate_radars
from .data_processing import data_user_activity, data_leaderboard, data_radar, data_weekly_levels, data_streaks_leaderboard
from . import dashboard_blueprint
import json
from flask_user import login_required


@dashboard_blueprint.route('/', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


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
    leaderboard_labels, leaderboard_data, current_user_rank, rank_up_data = data_leaderboard()

    all_leaderboard_data = dict(leaderboard_labels=leaderboard_labels,
                                leaderboard_data=leaderboard_data,
                                current_user_rank=current_user_rank,
                                rank_up_data=rank_up_data)

    return make_response(jsonify(all_leaderboard_data))


@dashboard_blueprint.route('/getweeklylevelsdata')
def get_weekly_levels_data():
    level_one, level_two, level_three = data_weekly_levels()

    all_weekly_levels_data = dict(level_one=level_one,
                                  level_two=level_two,
                                  level_three=level_three)

    return make_response(jsonify(all_weekly_levels_data))


@dashboard_blueprint.route('/gettopstreaksdata')
def get_top_streaks_data():
    usernames, top_streaks = data_streaks_leaderboard()

    top_streaks_data = dict(usernames=usernames,
                            top_streaks=top_streaks
                            )

    return make_response(jsonify(top_streaks_data))

