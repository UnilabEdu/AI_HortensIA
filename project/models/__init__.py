from datetime import datetime, date, timedelta
from project.database import db
from project.models.user import User
from sqlalchemy.sql.expression import func


class Emotion(db.Model):
    """
    contains emotion names, definitions, and similar words to the 33 predefined emotions in two languages
    users choose one of these emotions to mark a text and submit a ticket
    """
    __tablename__ = "emotions"
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(80), nullable=False, unique=True)
    name_ka = db.Column(db.String(80), nullable=False, unique=True)
    similar_ka = db.Column(db.String(80))
    similar_en = db.Column(db.String(80))
    definition_ka = db.Column(db.Text)
    definition_en = db.Column(db.Text)
    tickets = db.relationship('Ticket', backref='emotions')

    def __init__(self, name_ka, name_en, similar_ka, similar_en, definition_ka, definition_en):
        self.name_ka = name_ka
        self.name_en = name_en
        self.similar_ka = similar_ka
        self.similar_en = similar_en
        self.definition_ka = definition_ka
        self.definition_en = definition_en

    def __repr__(self):
        return f'Emotion object: {self.name_ka}, {self.name_en}'

    @classmethod
    def get_all(cls):
        return cls.query.all()


class Files(db.Model):
    """
    contains files from which the Text objects are gathered
    """
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    file_name = db.Column(db.String, nullable=False, unique=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    sentences = db.relationship('Text', backref='files')

    def __init__(self, title, file_name, user_id):
        self.title = title
        self.file_name = file_name
        self.user = user_id

    def __repr__(self):
        return f"File Object: title: {self.title} file_name: {self.file_name}. user: {self.user}"


class Text(db.Model):
    """
    contains texts (sentences or paragraphs) which would be marked by users
    """
    __tablename__ = "texts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    file = db.Column(db.Integer, db.ForeignKey('files.id'))
    tickets = db.relationship('Ticket', backref='texts')

    def __init__(self, text, file):
        self.text = text
        self.file = file

    def __repr__(self):
        return f"Text Object: file {self.file}. sentence: {self.text}. "

    @classmethod
    def get_random(cls):
        return cls.query.order_by(func.random()).first()


class Ticket(db.Model):
    """
    contains submitted tickets with data on the author of the ticket, the marked text, the chosen emotion, and the time
    """
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Integer, db.ForeignKey('texts.id'))
    emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
    date = db.Column(db.DateTime)

    def __init__(self, user_id, text_id, emotion_id, commit_date=datetime.now()):
        self.user = user_id
        self.text = text_id
        self.emotion = emotion_id
        self.date = commit_date

    def __repr__(self):
        return f'Ticket author:{self.user}; ticket text: {self.text}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ActivityStreak(db.Model):
    """
    contains each user's activity streaks: how many days in a row has a user submitted at least one ticket per day
    """
    __tablename__ = 'streaks'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    total_days = db.Column(db.Integer)
    status = db.Column(db.Boolean(), nullable=False)

    def __init__(self, user_id, start_date=date.today(), end_date=date.today(), total_days=1, status=1):
        self.user = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = total_days
        self.status = status

    def update_streak(self):
        """
        Returns Boolean which determines whether the Streak was valid or not
        If a Streak is invalid, a new streak should be created separately, using __init__
        """
        today = date.today()
        # Continuing a Streak
        if today - timedelta(days=1) == self.end_date:
            self.end_date = today
            self.total_days += 1
            db.session.commit()
            return True
        # When Streak was already continued today
        elif today == self.end_date:
            return True
        # When Streak was already broken and won't be continued
        else:
            self.status = 0
            db.session.commit()
            return False

    def __repr__(self):
        return f"ActivityStreak Object: start: {self.start_date}. end: {self.end_date}. " \
               f"status: {self.status}. User: {self.user}"


class SubscribedEmails(db.Model):
    """
    contains emails which should be added to the mailing list
    """
    __tablename__ = "subscribed_emails"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    def __init__(self, email, timestamp=datetime.now(), active=1):
        self.email = email
        self.timestamp = timestamp
        self.active = active

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
