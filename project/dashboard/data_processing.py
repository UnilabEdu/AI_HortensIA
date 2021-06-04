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

        user_tickets = pd.read_sql(Ticket.query.filter_by(user=str(current_user.id)).statement, db.engine)  # ~0.16 sec

        # TODO: test time with more entries
        # Alternate version just in case, using Pandas to filter. Time: 0.02 - 0.03 seconds (700 entries)
        # df = pd.read_sql_table('tickets', db.engine)
        # user_tickets = df.loc[df['user'] == str(current_user.id)]

        dates_month = [date.today() - timedelta(days=i) for i in range(30)]
        dates_heatmap = [date.today() - timedelta(days=i) for i in range(182)]
        dates_month.reverse()
        dates_heatmap.reverse()

        all_dates = user_tickets['date'].dt.date  # get datetimes, convert to pd date, sort values

        frequencies = [0] * 30
        frequencies_heatmap = [0] * 182
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

        print(f"{time.time() - start_time} seconds")

        return frequencies, dates_month, final


def leaderboard():
    # TODO: optimize an clean up
    # TODO: fix 10th user not appearing when current_user in top 10
    import pandas as pd
    from project.database import db
    from project import create_app
    from flask_user import current_user
    from project.models import UserModel
    from pychartjs.Color import JSLinearGradient, Hex

    with create_app().app_context():

        current_user_frequency = None
        current_user_placement = None

        tickets = pd.read_sql_table('tickets', db.engine)

        s = pd.DataFrame(tickets['user']).value_counts().sort_values(ascending=False)

        if (current_user.id,) not in s.index[:10] and Ticket.query.filter_by(user=current_user.id).first():
            print(s.index)
            print(list(s.index))
            print(current_user.id)
            x = list(s.index).index((str(current_user.id),))
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

        base_color = JSLinearGradient('ctx', 0, 0, 600, 0,
                                      (0, Hex("#F05B6E")),
                                      (1, Hex("#FCAB5A"))
                                      ).returnGradient()
        special_color = JSLinearGradient('ctx', 0, 0, 600, 0,
                                         (0, Hex("#FCAB5A")),
                                         (1, Hex("#F05B6E"))
                                         ).returnGradient()
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

        return usernames, frequencies, placements, colors
