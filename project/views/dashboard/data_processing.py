import datetime
from datetime import date, timedelta
from datetime import datetime

import pandas as pd
from flask_babel import lazy_gettext
from flask_user import current_user
from sqlalchemy.orm import load_only

from project import create_app
from project.database import db
from project.models import Ticket
from project.models import User, ActivityStreak


def data_user_activity():
    """
    calculates user activity data for the last 182 days
    returns a list with five nested elements:
    :frequencies: list that contains the amount of tickets current_user submitted on each day of the last 30 days
    :dates_month: list that contains the dates of each day of the last 30 days
    :final: dictionary with data needed to generate a heatmap (dates and values)
    :min_max: list with two items: minimal amount of tickets filled in the last 182 days and the maximum amount
    :day_streak: integer that indicates the current amount of active days in a row for current_user
    """
    with create_app().app_context():
        today = date.today()

        # get all tickets submitted by current_user
        user_tickets = pd.read_sql(Ticket.query.filter_by(user=current_user.id).statement, db.engine)

        # generate lists containing all dates from today to 30 days ago and 182 days ago
        dates_month = [today - timedelta(days=i) for i in range(30)]
        dates_heatmap = [today - timedelta(days=i) for i in range(182)]
        dates_month.reverse()
        dates_heatmap.reverse()

        raw_dates = user_tickets['date']
        nonzero_dates = len(raw_dates) > 0

        frequencies = [0] * 30
        frequencies_heatmap = [0] * 182
        if nonzero_dates:
            all_dates = user_tickets['date'].dt.date  # convert dates to python type date

            for day in all_dates:
                # get frequencies for this month
                try:
                    index = dates_month.index(day)
                    frequencies[index] += 1
                except ValueError:
                    pass

                # get frequencies for last 6 months
                try:
                    index = dates_heatmap.index(day)
                    frequencies_heatmap[index] += 1
                except ValueError:
                    pass

        # calculate the minimum and maximum frequency to better generate heatmap colors
        min_freq = min(frequencies_heatmap)
        max_freq = max(frequencies_heatmap)
        min_max = [min_freq, max_freq]

        # generate dictionary for heatmap data
        final = []
        week_numbers = [str(d.isoweekday()) for d in dates_heatmap]
        dates_heatmap = [str(d) for d in dates_heatmap]

        # heatmap chart receives a dictionary with x, y, d, v keys. x and d is the date, y is week number, v is value
        preset_dictionary = {'x': None, 'y': None, 'd': None, 'v': None}
        for x, y, v in zip(dates_heatmap, week_numbers, frequencies_heatmap):
            preset_dictionary.update(x=x, y=y, d=x, v=v)
            final.append(preset_dictionary.copy())

        dates_month = [str(d) for d in dates_month]  # convert to string to be able to display them

        current_streak = ActivityStreak.query.filter_by(user=current_user.id, status=1).first()  # select current streak

        if current_streak and current_streak.end_date == date.today():  # streak was already continued today
            day_streak = current_streak.total_days
        elif current_streak and current_streak.end_date == date.today() - timedelta(days=1):  # streak not continued yet
            day_streak = 0 - current_streak.total_days  # negative number is used to indicate that the streak is paused
        else:  # current streak expired
            day_streak = 0

        return frequencies, dates_month, final, min_max, day_streak


def data_leaderboard():
    """
    calculates data to display leaderboard-related data based on the highest amounts of submitted tickets by users
    returns a list with five nested elements:
    :usernames: list with usernames of top 10 users as strings and current_user's username if it wasn't already included
    :frequencies: list with the amount of submitted tickets by each of the top 10 users and current_user
    :current_user_rank: integer indicating current_user's rank in the global leaderboard based on submitted tickets
    :rank_up_data: list with two items: amount of tickets current_user is ahead of the user with previous rank and
    the amount of tickets needed to reach the next rank
    """
    with create_app().app_context():
        user_was_active = True
        current_user_frequency = None
        current_user_rank = None
        tickets_to_next_rank = 0
        tickets_ahead_of_previous = 0

        # Get IDs of every ticket's author
        tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user')).statement, db.engine)

        # Count the amount of tickets authored by each user ID and sort them
        s = pd.DataFrame(tickets['user']).value_counts().sort_values(ascending=False)

        # Get Top 10 users, their IDs and amount of filled tickets
        top_ten = s.head(10)
        user_ids = [i[0] for i in top_ten.index.tolist()]
        frequencies = top_ten.values.tolist()

        # Get usernames for the Top 10 users
        usernames = []
        count = 1
        for u in user_ids:
            usernames.append('   ' + str(count) + '. ' + User.query.get.username.capitalize())
            count += 1

        # Check if current_user is in Top 10 and whether they have at least one post
        if current_user.id not in user_ids and Ticket.query.filter_by(user=current_user.id).first():
            # Determine current_user's index in the list of users sorted by filled tickets
            x = list(s.index).index((current_user.id,))
            # Get the amount of tickets filled by current_user and append to other users' frequencies
            current_user_frequency = int(s.values[x])
            frequencies.append(current_user_frequency)
            # Increment x because list indices start with 0
            current_user_rank = x + 1
            # Add a label to current_user's column,
            usernames.append(f"   {current_user_rank}. " + lazy_gettext("YOU     ➤"))

        elif current_user.id in user_ids:
            x = user_ids.index(current_user.id)
            current_user_rank = x + 1
            # Change current_user's label
            usernames[x] = f"   {str(x + 1)}. " + lazy_gettext("YOU     ➤")

        # Else happens when current_user has 0 filled tickets
        else:
            user_was_active = False

        if user_was_active:
            if current_user_rank == 1:
                current_user_frequency = frequencies[current_user_rank - 1]
                tickets_to_next_rank = 'leader'

            elif current_user.id in user_ids:
                current_user_frequency = frequencies[current_user_rank - 1]
                tickets_to_next_rank = int(s.iloc[current_user_rank - 2]) - current_user_frequency + 1

            else:
                tickets_to_next_rank = int(s.iloc[current_user_rank - 2]) - current_user_frequency + 1

            if len(s) > current_user_rank:
                tickets_ahead_of_previous = current_user_frequency - int(s.iloc[current_user_rank])
            else:
                tickets_ahead_of_previous = current_user_frequency

        rank_up_data = [tickets_ahead_of_previous, tickets_to_next_rank]

        return usernames, frequencies, current_user_rank, rank_up_data


def data_radar():
    """
    calculate data necessary to display two radar charts (one with 8 primary emotions, one with 8 secondary)
    includes data for 4 timeframes for both charts: any time, last month, last week, today
    separates data into current_user's data and everyone's data
    returns a list with two nested lists: 'final_primary' and 'final_secondary'
    the nested lists have this structure each: the first 4 items are everyone's data for 4 timeframes
    the last 4 items contain only current_user's data for 4 timeframes
    this sums up to 8 nested lists in 'final_primary' and 'final_secondary' each
    """

    with create_app().app_context():

        today = date.today()

        # Get all tickets
        all_tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user', 'emotion', 'date')).statement,
                                  db.engine)

        if len(all_tickets) == 0:  # abort to avoid an error if there are 0 tickets, return zeroes for everything
            return [[0] * 8, [0] * 8]

        all_tickets['date'] = all_tickets['date'].dt.date  # Change date format of all tickets

        # Get all current_user tickets
        user_tickets = all_tickets.loc[all_tickets['user'] == current_user.id]

        # Make dataframes for different time periods (day/week/month) for all data and for current_user
        all_month_tickets = all_tickets.loc[all_tickets['date'] >= (today - timedelta(days=30))]
        all_week_tickets = all_tickets.loc[all_tickets['date'] >= (today - timedelta(days=7))]
        all_day_tickets = all_tickets.loc[all_tickets['date'] >= (today - timedelta(days=1))]

        user_month_tickets = user_tickets.loc[user_tickets['date'] >= (today - timedelta(days=30))]
        user_week_tickets = user_tickets.loc[user_tickets['date'] >= (today - timedelta(days=7))]
        user_day_tickets = user_tickets.loc[user_tickets['date'] >= (today - timedelta(days=1))]

        # Get dataframes ready to be iterated over
        all_dataframes = [all_tickets, all_month_tickets, all_week_tickets, all_day_tickets,
                          user_tickets, user_month_tickets, user_week_tickets, user_day_tickets]

        # For each df: get percentages of each emotion, convert them to coefficients and emotion group coefficients
        final_primary = []  # data for 8 emotion groups out of the first 24 (primary) emotions
        final_secondary = []  # data for 8 last (secondary) emotions
        for df in all_dataframes:
            # Get percentages of emotions, sorted by emotion
            df = df.emotion.value_counts(normalize=True).sort_index()

            # Convert the pd.Series object to a list
            emotion_percentages = df.to_list()

            # Check if there are any missing emotions
            present_emotions = df.index.to_list()
            if len(present_emotions) != 34:
                # Find out which emotions are missing
                missing_emotions = [e for e in range(1, 34) if e not in present_emotions]

                # Fill indices corresponding to missing emotions with zeroes
                for i in missing_emotions:
                    emotion_percentages.insert(i - 1, 0)  # Now the previously missing emotions have value 0

            # Calculate coefficients of the 8 groups of primary emotions, append the groups and the remaining 8 emotions
            count = 1
            current_emotion_group = []  # group of 3 similar emotions
            current_primary_frequencies = []  # final coefficients for all groups of primary emotions in this dataframe
            current_secondary_frequencies = []  # final percentages for all secondary emotions in this dataframe
            for i in emotion_percentages:
                if count <= 24:  # primary emotions
                    if count % 3 == 0:  # third emotion, end of the emotion group
                        current_emotion_group.append(i * 0.6)
                        current_primary_frequencies.append(round(sum(current_emotion_group * 100), 2))
                        current_emotion_group = []
                    elif (count + 1) % 3 == 0:  # second emotion
                        current_emotion_group.append(i * 0.8)
                    else:  # first (the most intense) emotion
                        current_emotion_group.append(i)
                    count += 1
                else:
                    current_secondary_frequencies.append(round(i * 100, 200))

            final_primary.append(current_primary_frequencies)
            final_secondary.append(current_secondary_frequencies[:-1])

        return final_primary, final_secondary


def data_weekly_levels():
    """
    ca
    """
    with create_app().app_context():

        users_week_frequencies = pd.read_sql(Ticket.query
                                             .options(load_only('user'))
                                             .filter(Ticket.date > datetime.now() - timedelta(days=7))
                                             .statement, db.engine)

        users_week_counts_dict = pd.DataFrame(users_week_frequencies['user']).value_counts().to_dict()

        level_three_users = []
        level_two_users = []
        level_one_users = []
        for user, count in users_week_counts_dict.items():
            if count > 105:
                level_three_users.append([user[0], count])
            elif count > 70:
                level_two_users.append([user[0], count])
            elif count > 35:
                level_one_users.append([user[0], count])

        level_three_users = [[User.query.get.username.capitalize(), i[1]] for i in level_three_users]
        level_two_users = [[User.query.get.username.capitalize(), i[1]] for i in level_two_users]
        level_one_users = [[User.query.get.username.capitalize(), i[1]] for i in level_one_users]

        return level_one_users, level_two_users, level_three_users


def data_streaks_leaderboard():
    with create_app().app_context():
        all_streaks = pd.read_sql(db.session.query(ActivityStreak).options(load_only('user', 'total_days')).statement,
                                  db.engine).drop(columns='id')
        all_streaks = all_streaks.sort_values('total_days', ascending=False).head(10)

        usernames = []
        count = 1
        for user_id in all_streaks.user.to_list():
            usernames.append('   ' + str(count) + '. ' + User.query.get.username.capitalize())
            count += 1

        top_streaks = all_streaks.total_days.to_list()

        return usernames, top_streaks
