from flask_user import current_user
import pandas as pd
from project import create_app
from project.database import db
from project.models import Ticket
import time
from datetime import date, timedelta


def data_user_line():
    with create_app().app_context():
        start_time = time.time()  # Only to measure time of execution. Remove later
        # TODO: use load_only

        # TODO: why did user=str(current_user.id) still work here?
        user_tickets = pd.read_sql(Ticket.query.filter_by(user=current_user.id).statement, db.engine)  # ~0.16 sec

        # TODO: test time with more entries
        # Alternate version just in case, using Pandas to filter. Time: 0.02 - 0.03 seconds (700 entries)
        # df = pd.read_sql_table('tickets', db.engine)
        # user_tickets = df.loc[df['user'] == current_user.id]

        dates_month = [date.today() - timedelta(days=i) for i in range(30)]
        dates_heatmap = [date.today() - timedelta(days=i) for i in range(182)]
        dates_month.reverse()
        dates_heatmap.reverse()

        all_dates = user_tickets['date'].dt.date  # get datetimes, convert to pd date, sort values

        frequencies = [0] * 30
        frequencies_heatmap = [0] * 182
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

        return frequencies, dates_month, final


def leaderboard():
    # TODO: optimize an clean up
    # TODO: fix 10th user not appearing when current_user in top 10
    import pandas as pd
    from project.database import db
    from project import create_app
    from flask_user import current_user
    from project.models import UserModel
    from pychartjs.Color import RGBA, Hex

    with create_app().app_context():
        start_time = time.time()  # Only to measure time of execution. Remove later

        current_user_frequency = None
        current_user_placement = None

        tickets = pd.read_sql_table('tickets', db.engine)

        s = pd.DataFrame(tickets['user']).value_counts().sort_values(ascending=False)

        if (current_user.id,) not in s.index[:10] and Ticket.query.filter_by(user=current_user.id).first():
            x = list(s.index).index((current_user.id,))
            current_user_frequency = int(s.values[x])
            current_user_placement = x + 1

        # s = s.sort_values(ascending=False).head(10).reset_index()
        s = s.head(10)
        user_ids = [i[0] for i in s.index.tolist()]
        frequencies = s.values.tolist()

        usernames = []
        for i in user_ids:
            usernames.append(UserModel.query.get(i).username.capitalize())

        if current_user.username.capitalize() not in usernames:
            usernames.append("YOU ➤    ")

        base_color = RGBA(127, 92, 194, 1)
        special_color = RGBA(156, 92, 194, 1)
        colors = [base_color] * len(usernames)

        if len(usernames) == 10:
            current_user_index = usernames.index(current_user.username.capitalize())
            colors[current_user_index] = special_color
        else:
            colors[10] = special_color

        placements = [str(i) + '. ' for i in list(range(1, 11))]

        if current_user_placement and current_user_frequency:
            placements.append(str(current_user_placement) + '. ')
            frequencies.append(current_user_frequency)

        print(f"LEADERBOARD TIME: {time.time() - start_time} seconds")

        return usernames, frequencies, placements, colors
        # base_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                               (0, Hex("#F05B6E")),
        #                               (1, Hex("#FCAB5A"))
        #                               ).returnGradient()
        # special_color = JSLinearGradient('ctx', 0, 0, 600, 0,
        #                                  (0, Hex("#FCAB5A")),
        #                                  (1, Hex("#F05B6E"))
        #                                  ).returnGradient()


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
        # class current_user:
        #     id = 2

        # Get all tickets
        all_tickets = pd.read_sql(db.session.query(Ticket).options(load_only('user', 'emotion', 'date')).statement, db.engine)
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
                    emotion_percentages.insert(i-1, 0)  # Now the previously missing emotions have value 0

            # Calculate coefficients of the 8 groups of primary emotions, append the groups and the remaining 8 emotions
            count = 1
            current_emotion_group = []  # group of 3 similar emotions
            current_primary_frequencies = []  # final coefficients for all groups of primary emotions in this dataframe
            current_secondary_frequencies = []  # final percentages for all secondary emotions in this dataframe
            for i in emotion_percentages:
                if count <= 24:  # primary emotions
                    if count % 3 == 0:  # third emotion, end of the emotion group
                        current_emotion_group.append(i * 0.6)
                        current_primary_frequencies.append(round(sum(current_emotion_group*100), 2))
                        current_emotion_group = []
                    elif (count + 1) % 3 == 0:  # second emotion
                        current_emotion_group.append(i * 0.8)
                    else:  # first (the most intense) emotion
                        current_emotion_group.append(i)
                    count += 1
                else:
                    current_secondary_frequencies.append(round(i*100, 2))

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
