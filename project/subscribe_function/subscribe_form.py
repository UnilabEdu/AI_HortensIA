from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, Email
from flask_babel import lazy_gettext


class SubscribeForm(FlaskForm):
    email = StringField("ელექტრონული ფოსტა", [DataRequired(), length(min=4), Email()],
                        render_kw={"placeholder": lazy_gettext("ელ-ფოსტა")})
    submit = SubmitField(lazy_gettext("გამოწერა"))

