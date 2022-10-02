from flask import render_template, make_response, jsonify
from flask_user import login_required
from .data_processing import data_user_activity, data_leaderboard, data_radar, data_weekly_levels, \
    data_streaks_leaderboard

from flask import Blueprint

dashboard_blueprint = Blueprint('dashboard',
                                __name__,
                                template_folder='templates',
                                static_folder='static'
                                )



@dashboard_blueprint.route('/', methods=['GET'])
@login_required
def dashboard():
    """
    renders a dashboard with charts based on current_user's contributions
    charts use data from get_radars_data, get_activity_data, get_leaderboard_data,
    get_weekly_levels_data, and get_top_streaks_data endpoints using JavaScript
    """
    return render_template('dashboard/dashboard.html')


@dashboard_blueprint.route('/getradarsdata')
def get_radars_data():
    """
    returns a JSON which contains all of the data needed in radar charts
    the JSON has 8 keys based on the time (all time, month, week, today) and who the data belongs to (user or everyone)
    """
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
    """
    returns a JSON with data to be displayed on the heatmap, month/week chart, and current streak chart (donut)
    :min_max: is used to generate heatmap colors better (based on normalized data)
    """
    data_month_frequencies, data_month_labels, heatmap_data, min_max, streak = data_user_activity()

    month_chart_labels = data_month_labels
    month_chart_frequencies = data_month_frequencies

    all_activity_chart_data = dict(month_chart_labels=month_chart_labels,
                                   month_chart_frequencies=month_chart_frequencies,
                                   heatmap_data=heatmap_data,
                                   min_max=min_max,
                                   streak=streak)

    return make_response(jsonify(all_activity_chart_data))


@dashboard_blueprint.route('/getleaderboarddata')
def get_leaderboard_data():
    """
    returns a JSON with top 10 users based on the amount of Tickets filled to display on a chart
    includes current_user data even if current_user isn't in the top 10
    """
    leaderboard_labels, leaderboard_data, current_user_rank, rank_up_data = data_leaderboard()

    all_leaderboard_data = dict(leaderboard_labels=leaderboard_labels,
                                leaderboard_data=leaderboard_data,
                                current_user_rank=current_user_rank,
                                rank_up_data=rank_up_data)

    return make_response(jsonify(all_leaderboard_data))


@dashboard_blueprint.route('/getweeklylevelsdata')
def get_weekly_levels_data():
    """
    returns a JSON with last week's activity data grouped by three levels to display on tables
    """
    level_one, level_two, level_three = data_weekly_levels()

    all_weekly_levels_data = dict(level_one=level_one,
                                  level_two=level_two,
                                  level_three=level_three)

    return make_response(jsonify(all_weekly_levels_data))


@dashboard_blueprint.route('/gettopstreaksdata')
def get_top_streaks_data():
    """
    returns a JSON with top 10 ActivityStreaks data to display on a chart
    """
    usernames, top_streaks = data_streaks_leaderboard()

    top_streaks_data = dict(usernames=usernames,
                            top_streaks=top_streaks
                            )

    return make_response(jsonify(top_streaks_data))
