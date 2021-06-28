from wtforms import SelectField, SubmitField
from flask_wtf import FlaskForm
from project.emotions_list import emotions


class EmotionForm(FlaskForm):
    emotion = SelectField('Emotion',
                          choices=[(num, emotions[num]) for num in range(len(emotions))])
    submit = SubmitField('Submit')
