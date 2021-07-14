from project.models import ActivityStreak
from project.database import db
from project import create_app

with create_app(import_blueprints=False).app_context():
    # db.session.add(ActivityStreak(123))
    # db.session.commit()
    # db.session.close()

    ActivityStreak.query.get(2).update_streak()
