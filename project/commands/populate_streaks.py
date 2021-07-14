from project.models import ActivityStreak
from project.database import db
from project import create_app
import random
from datetime import date, timedelta

with create_app(import_blueprints=False).app_context():
    for i in range(10000):
        start_date = date.today() - timedelta(days=random.randrange(1, 100))
        total_days = random.randrange(1, 100)
        end_date = start_date + timedelta(days=total_days)

        db.session.add(ActivityStreak(
                            user_id=random.randrange(1, 301),
                            start_date=start_date,
                            end_date=end_date,
                            total_days=total_days,
                            status=1
                            )
                       )

    db.session.commit()
