import datetime

from flask_user import current_user
import pandas as pd
from sqlalchemy import text

from project import create_app
from project.database import db
from project.models import Ticket
import time
from datetime import date, timedelta, datetime


def data_user_activity():
    with create_app(import_blueprints=False).app_context():
        start_time = time.time()  # Only to measure time of execution. Remove later
        # TODO: use load_only

        # TODO: Delete me later (only for testing) also remove import blueprints
        # class current_user:
        #     id = 1
        #     username = 'User_Opt.335'

        today = date.today()

        # TODO: why did user=str(current_user.id) still work here?
        user_tickets = pd.read_sql(Ticket.query.filter_by(user=current_user.id).statement, db.engine)  # ~0.16 sec

        # TODO: test time with more entries
        # Alternate version just in case, using Pandas to filter. Time: 0.02 - 0.03 seconds (700 entries)
        # df = pd.read_sql_table('tickets', db.engine)
        # user_tickets = df.loc[df['user'] == current_user.id]

        dates_month = [today - timedelta(days=i) for i in range(30)]
        dates_heatmap = [today - timedelta(days=i) for i in range(182)]
        dates_month.reverse()
        dates_heatmap.reverse()

        raw_dates = user_tickets['date']
        nonzero_dates = len(raw_dates) > 0

        all_dates = []
        frequencies = [0] * 30
        frequencies_heatmap = [0] * 182
        if nonzero_dates:
            all_dates = user_tickets['date'].dt.date  # get datetimes, convert to pd date, sort values

            # TODO: remove 'try: , except ValueError'
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

        # generate dictionary for heatmap data
        final = []
        week_numbers = [str(d.isoweekday()) for d in dates_heatmap]
        dates_heatmap = [str(d) for d in dates_heatmap]

        preset_dictionary = {'x': None, 'y': None, 'd': None, 'v': None}
        for x, y, v in zip(dates_heatmap, week_numbers, frequencies_heatmap):
            preset_dictionary.update(x=x, y=y, d=x, v=v)
            final.append(preset_dictionary.copy())

        print(f"LINE CHARTS TIME: {time.time() - start_time} seconds")

        # print('____________________MONTH LABELS (DATES) DATA:\n', dates_month)
        # print('____________________MONTH FREQUENCIES DATA:\n', frequencies)

        dates_month = [str(d) for d in dates_month]

        # ADDITIONAL ACTIVITY STATS START HERE

        # STREAKS
        # TODO: remove this function as it's obsolete now: streaks shouldn't be calculated later -- they should be created, stored in a DB and updated constantly
        def calculate_streak(today_or_yesterday):
            check_day = today - timedelta(days=today_or_yesterday)
            day_streak = 0
            if nonzero_dates:
                while check_day in all_dates.to_list():
                    day_streak += 1
                    check_day = check_day - timedelta(days=1)
                print(day_streak)
                # TODO: when done testing or when there's today's data in DB, change 8 to 1 and 7 to 0 below (in the next ~7 lines)
                if today_or_yesterday == 8:
                    day_streak = 0 - day_streak
            return day_streak

        day_streak = calculate_streak(7)
        if day_streak == 0:
            day_streak = calculate_streak(8)

        print(f"NEW FUNCTIONS TIME: {time.time() - start_time} seconds")

        print(frequencies[-7:])
        print(sum(frequencies[-7:]))
        print(len(frequencies[-7:]))

        print(f'FREQ: {frequencies} \n DATES_M: {dates_month} \n FINAL(HEAT): {final} \n STREAK: {day_streak}')
        return frequencies, dates_month, final, day_streak


# data_user_activity()


def data_leaderboard_optimized():
    # TODO: handle long usernames
    import pandas as pd
    from project.database import db
    from project import create_app
    # from flask_user import current_user
    from project.models import User
    from sqlalchemy.orm import load_only

    with create_app(import_blueprints=False).app_context():

        # # TODO: Delete me later (only for testing) also remove import blueprints, also uncomment import current_user
        # class current_user:
        #     id = 1
        #     username = 'User_Argati1870'

        current_user = User.query.get(1)

        start_time = time.time()  # Only to measure time of execution. Remove later

        user_was_active = True
        current_user_frequency = None
        current_user_rank = None
        tickets_to_next_rank = 0
        tickets_ahead_of_previous = 0

        t0 = time.time()
        # Make a query for Users and Amount of Filled Tickets sorted by descending
        users_ticket_count = db.session.query(User, db.func.count(User.tickets).label('total')).outerjoin(
            Ticket).group_by(User).order_by(text('total DESC'))
        print(time.time() - t0)
        # print('started ;)')

        # TODO: handle zero filled tickets (again)
        # Get Top 10 users
        t1 = time.time()
        # top_ten = users_ticket_count[:1]
        print(time.time() - t1)
        t2 = time.time()
        top_ten = users_ticket_count[:10]
        print(time.time() - t2)


        # Get usernames for the Top 10 users
        usernames = []
        frequencies = []
        count = 1
        for user, frequency in top_ten:
            usernames.append('   ' + str(count) + '. ' + user.username)
            frequencies.append(frequency)
            count += 1

        # Get user frequency and rank
        current_user_frequency = users_ticket_count.filter_by(user=1).first()[1]
        current_user_rank = [user[0] for user in users_ticket_count].index(current_user) + 1  # THIS STATEMENT TAKES TOO MUCH TIME

        frequencies.append(current_user_frequency)
        usernames.append(f"   {current_user_rank}. YOU     ➤")

        tickets_to_next_rank = users_ticket_count[current_user_rank-2][1] - current_user_frequency + 1  # THIS STATEMENT TAKES TOO MUCH TIME
        tickets_ahead_of_previous = current_user_frequency - users_ticket_count[current_user_rank][1]  # THIS STATEMENT TAKES TOO MUCH TIME



        # # Get IDs of every ticket's author
        # tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user')).statement, db.engine)
        # user = pd.read_sql(db.session.query(UserModel).statement, db.engine)
        #
        # # Count the amount of tickets authored by each user ID and sort them
        # s = pd.DataFrame(tickets['user']).value_counts().sort_values(ascending=False)
        #
        # # Get Top 10 users, their IDs and amount of filled tickets
        # top_ten = s.head(10)


        # TODO: what if user hasn't filled a single ticket?
        # Check if current_user is in Top 10 and whether they have at least one post
        # if current_user.id not in user_ids and Ticket.query.filter_by(user=current_user.id).first():
        #     # Determine current_user's index in the list of users sorted by filled tickets
        #     x = list(s.index).index((current_user.id,))
        #     # Get the amount of tickets filled by current_user and append to other users' frequencies
        #     current_user_frequency = int(s.values[x])
        #     frequencies.append(current_user_frequency)
        #     # Increment x because list indices start with 0
        #     current_user_rank = x + 1
        #     # Add a label to current_user's column,
        #     usernames.append(f"   {current_user_rank}. YOU     ➤")
        # elif current_user.id in user_ids:
        #     x = user_ids.index(current_user.id)
        #     current_user_rank = x + 1
        #     # Change current_user's label
        #     usernames[x] = f"   {str(x + 1)}. YOU     ➤"

        # # Else happens when current_user has 0 filled tickets
        # else:
        #     user_was_active = False

        # if user_was_active:
        #     # TODO: add comments
        #     tickets_to_next_rank = int(s.iloc[current_user_rank - 2]) - current_user_frequency + 1
        #     tickets_ahead_of_previous = current_user_frequency - int(s.iloc[current_user_rank])

        rank_up_data = [tickets_ahead_of_previous, tickets_to_next_rank]
        print(f"\n\n\nLEADERBOARD TIME (NEW): {time.time() - start_time} seconds")

        # print(f'Results: usernames: {usernames} \n frequencies: {frequencies} \n rankings: {current_user_rank}')
        return usernames, frequencies, current_user_rank, rank_up_data
        # base_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                               (0, Hex("#F05B6E")),
        #                               (1, Hex("#FCAB5A"))
        #                               ).returnGradient()
        # special_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                                  (0, Hex("#FCAB5A")),
        #                                  (1, Hex("#F05B6E"))
        #                                  ).returnGradient()


# data_leaderboard_optimized()


def data_leaderboard():
    # TODO: handle long usernames
    import pandas as pd
    from project.database import db
    from project import create_app
    # from flask_user import current_user
    from project.models import User
    from sqlalchemy.orm import load_only

    with create_app(import_blueprints=False).app_context():

        # # TODO: Delete me later (only for testing) also remove import blueprints, also uncomment import current_user
        # class current_user:
        #     id = 1
        #     username = 'User_Argati1870'

        current_user = User.query.get(1)

        start_time = time.time()  # Only to measure time of execution. Remove later

        user_was_active = True
        current_user_frequency = None
        current_user_rank = None
        tickets_to_next_rank = 0
        tickets_ahead_of_previous = 0

        # Get IDs of every ticket's author
        tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user')).statement, db.engine)
        user = pd.read_sql(db.session.query(User).statement, db.engine)
        # print(user.tickets)

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
            usernames.append('   ' + str(count) + '. ' + User.query.get(u).username.capitalize())
            count += 1

        # TODO: what if user hasn't filled a single ticket?
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
            usernames.append(f"   {current_user_rank}. YOU     ➤")
        elif current_user.id in user_ids:
            x = user_ids.index(current_user.id)
            current_user_rank = x + 1
            # Change current_user's label
            usernames[x] = f"   {str(x + 1)}. YOU     ➤"

        # Else happens when current_user has 0 filled tickets
        else:
            user_was_active = False

        if user_was_active:
            # TODO: add comments
            tickets_to_next_rank = int(s.iloc[current_user_rank - 2]) - current_user_frequency + 1
            tickets_ahead_of_previous = current_user_frequency - int(s.iloc[current_user_rank])

            # print(s[current_user_rank-5:current_user_rank+5])

        rank_up_data = [tickets_ahead_of_previous, tickets_to_next_rank]

        print(rank_up_data)

        print(f"\n\n\nLEADERBOARD TIME (NEW): {time.time() - start_time} seconds")

        # print(f'Results: usernames: {usernames} \n frequencies: {frequencies} \n rankings: {current_user_rank}')
        return usernames, frequencies, current_user_rank, rank_up_data
        # base_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                               (0, Hex("#F05B6E")),
        #                               (1, Hex("#FCAB5A"))
        #                               ).returnGradient()
        # special_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                                  (0, Hex("#FCAB5A")),
        #                                  (1, Hex("#F05B6E"))
        #                                  ).returnGradient()

# data_leaderboard()


def data_radar():
    import pandas as pd
    from project.database import db
    from project import create_app
    from datetime import date, timedelta
    from sqlalchemy.orm import load_only

    with create_app(import_blueprints=False).app_context():
        start_time = time.time()  # Only to measure time of execution. Remove later

        today = date.today()

        # Remove this and import_blueprints when running server
        class current_user:
            id = 2

        # Get all tickets
        all_tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user', 'emotion', 'date')).statement,
                                  db.engine)
        # all_tickets = pd.read_sql(db.session.query(Ticket).filter(Ticket.emotion <= 45).options(load_only('user', 'emotion', 'date')).statement, db.engine)

        # Change date format of all tickets
        all_tickets['date'] = all_tickets['date'].dt.date
        # TODO: might remove current_user data (make radar charts be my data vs others' data instead of my data vs all data)
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
            if len(present_emotions) != 32:
                # Find out which emotions are missing
                missing_emotions = [e for e in range(1, 33) if e not in present_emotions]

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
                    current_secondary_frequencies.append(round(i * 100, 2))

            final_primary.append(current_primary_frequencies)
            final_secondary.append(current_secondary_frequencies)

        print(f"RADARS TIME: {time.time() - start_time} seconds")

        # Returns 2 lists, each with data on primary and secondary emotions, both containing 8 nested lists
        # First 4 elements (out of 8 nested lists) contain coefficients (or %) based on everyone's data in this order:
        # any time/ last month/ week/ day. Last 4 elements have the same structure but only include current_user's data
        return final_primary, final_secondary

# data_radar()
#
# final_primary, final_secondary = data_radar()
# print('___________FINAL__________________PRIMARY____________')
# count = 0
# for l in final_primary:
#     print(f'\n\n\n\n List index: {count} \n\n. List: {l}')
#     count += 1
# print('___________FINAL__________________SECONDARY____________')
# count = 0
# for l in final_secondary:
#     print(f'\n\n\n\n List index: {count} \n\n. List: {l}')
#     count += 1


# def data_radar():
#     import pandas as pd
#     from project.database import db
#     from project import create_app
#
#     with create_app(import_blueprints=False).app_context():
#         start_time = time.time()  # Only to measure time of execution. Remove later
#
#         # Remove this and import_blueprints when running server
#         class current_user:
#             id = 2
#
#         user_tickets = pd.read_sql(
#             db.session.query(Ticket).filter(Ticket.user == current_user.id, Ticket.emotion <= 24).statement, db.engine)
#         all_tickets = pd.read_sql(db.session.query(Ticket).filter(Ticket.emotion <= 24).statement, db.engine)
#         # user_tickets = pd.read_sql(Ticket.query.filter_by(user=current_user.id).statement, db.engine)  # ~0.16 sec
#         # all_tickets = pd.read_sql_table('tickets', db.engine)
#
#         emotions_list_user = list(range(1, 33))
#         emotions_list_all = list(range(1, 33))
#
#
#
#         user_tickets = user_tickets['emotion'].astype('int32')
#         all_tickets = all_tickets['emotion'].astype('int32')
#
#
#         user_tickets_missing = []
#         all_tickets_missing = []
#
#
#         for n in emotions_list_user:
#             if n not in user_tickets.tolist():
#                 user_tickets_missing.append(n)
#
#
#         for n in emotions_list_all:
#             if n not in all_tickets.tolist():
#                 all_tickets_missing.append(n)
#
#
#
#
#
#
#         user_tickets = user_tickets.value_counts(normalize=True).sort_index()
#         all_tickets = all_tickets.value_counts(normalize=True).sort_index()
#
#
#         # user_missing_dfs = pd.DataFrame([list(i).append(0) for i in user_tickets_missing])
#
#
#         # all_missing_dfs = pd.DataFrame([list(i).append(0) for i in all_tickets_missing])
#
#
#         # user_tickets.index[23] =
#         # print('HERE', user_tickets.index[22])
#
#
#         user_frequencies = []
#         user_frequencies_ones = []
#         user_frequencies_twos = []
#         user_frequencies_threes = []
#
#         all_frequencies = []
#         all_frequencies_ones = []
#         all_frequencies_twos = []
#         all_frequencies_threes = []
#
#         print('HERE::::::::::::::::::::::::: \n', user_tickets)
#         for index, value in user_tickets.iteritems():
#             # if emotions_list_user[0] == index:
#             #     emotions_list_user.remove(index)
#             #     print('Yes!', index)
#             # else:
#             #     user_tickets_missing.append(emotions_list_user[0])
#             #     emotions_list_user.remove(emotions_list_user[0])
#             #     print('NO!', index)
#
#             if index % 3 == 0:
#                 user_frequencies_threes.append(value * (1.5/3))
#             elif (index + 1) % 3 == 0:
#                 user_frequencies_twos.append(value * (2/3))
#             else:
#                 user_frequencies_ones.append(value)
#
#         for index, value in all_tickets.iteritems():
#             # if emotions_list_all[0] == index:
#             #     emotions_list_all.remove(index)
#             #     print('Yes!', index)
#             # else:
#             #     all_tickets_missing.append(emotions_list_all[0])
#             #     emotions_list_all.remove(emotions_list_all[0])
#             #     print('NO!', index)
#
#             if index % 3 == 0:
#                 all_frequencies_threes.append(value * (1.5/3))
#             elif (index + 1) % 3 == 0:
#                 all_frequencies_twos.append(value * (2/3))
#             else:
#                 all_frequencies_ones.append(value)
#
#         for one, two, three in zip(user_frequencies_ones, user_frequencies_twos, user_frequencies_threes):
#             user_frequencies.append(sum((one, two, three)))
#
#         for one, two, three in zip(all_frequencies_ones, all_frequencies_twos, all_frequencies_threes):
#             all_frequencies.append(sum((one, two, three)))
#
#
#         print(user_frequencies)
#         print(len(user_frequencies))
#         print(all_frequencies)
#         print(len(all_frequencies))
#
#         # print(user_tickets)
#         # print(all_tickets)
#
#         print(f"{time.time() - start_time} seconds")
#
#         # print(user_tickets_missing)
#         # print(all_tickets_missing)
#
#         user_frequencies = [i * 100 for i in user_frequencies]
#         all_frequencies = [i * 100 for i in all_frequencies]
#
#         return user_frequencies, all_frequencies


# data_radar()

def data_weekly_levels():
    import pandas as pd
    from project.database import db
    from project import create_app
    from project.models import User
    from sqlalchemy.orm import load_only

    with create_app(import_blueprints=False).app_context():
        # TODO: CHANGE TIMEDELTA DAYS=1 TO DAYS=7 (after done testing)
        start_time = time.time()  # Only to measure time of execution. Remove later

        users_week_frequencies = pd.read_sql(Ticket.query.options(load_only('user')).filter(Ticket.date > datetime.now() - timedelta(days=7)).statement, db.engine)
        users_week_counts_dict = pd.DataFrame(users_week_frequencies['user']).value_counts().to_dict()

        level_three_users = []
        level_two_users = []
        level_one_users = []
        for user, count in users_week_counts_dict.items():  # TODO: use proper brackets: 105, 70, 35. (200, 150, 100 is only for testing)
            if count > 200:
                level_three_users.append([user[0], count])
            elif count > 150:
                level_two_users.append([user[0], count])
            elif count > 25:
                level_one_users.append([user[0], count])
        # TODO: else stop iterating because values are sorted. Why are values sorted without sort_values()  (PD function)?

        # TODO: Optimize this part (next 3 lines)
        level_three_users = [[User.query.get(i[0]).username.capitalize(), i[1]] for i in level_three_users]
        level_two_users = [[User.query.get(i[0]).username.capitalize(), i[1]] for i in level_two_users]
        level_one_users = [[User.query.get(i[0]).username.capitalize(), i[1]] for i in level_one_users]

        print(level_three_users)
        print(len(level_three_users))

        print(level_two_users)
        print(len(level_two_users))

        print(level_one_users)
        print(len(level_one_users))



        print(users_week_counts_dict)
        print(len(users_week_counts_dict))

        print('TIME: ', time.time() - start_time)

        # TODO: change activity calculations to be the same as this function's methods: get frequencies based on datetimes, not just dates (firstly check if it's wrong now)

        return level_one_users, level_two_users, level_three_users


# data_weekly_levels()


def data_streaks_leaderboard():
    import pandas as pd
    from project.database import db
    from project import create_app
    # from flask_user import current_user
    from project.models import User, ActivityStreak
    from sqlalchemy.orm import load_only

    with create_app(import_blueprints=False).app_context():
        # # TODO: Delete me later (only for testing) also remove import blueprints, also uncomment import current_user
        # class current_user:
        #     id = 1
        #     username = 'User_Argati1870'

        current_user = User.query.get(1)

        start_time = time.time()

        all_streaks = pd.read_sql(db.session.query(ActivityStreak).options(load_only('user', 'total_days')).statement, db.engine).drop(columns='id')
        all_streaks = all_streaks.sort_values('total_days', ascending=False).head(10)

        usernames = []
        count = 1
        for user_id in all_streaks.user.to_list():
            usernames.append('   ' + str(count) + '. ' + User.query.get(user_id).username.capitalize())
            count += 1

        top_streaks = all_streaks.total_days.to_list()

        print('ACTIVITYSTREAKS TIME: ', time.time() - start_time, ' seconds')

        return usernames, top_streaks
