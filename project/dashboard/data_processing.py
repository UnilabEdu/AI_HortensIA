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

        empty_dates_month = [date.today() - timedelta(days=i) for i in range(30)]
        empty_dates_month.reverse()

        month_dates = user_tickets['date'].dt.date  # get datetimes, convert to date, sort values

        # print(empty_dates)
        frequencies = [0] * 30
        for day in month_dates:
            # if day in empty_dates_month:
            try:
                index = empty_dates_month.index(day)
                frequencies[index] += 1
            except ValueError:
                pass

        print(f"{time.time() - start_time} seconds")

        return frequencies, empty_dates_month
