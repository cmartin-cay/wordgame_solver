from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SubmitForm(FlaskForm):
    letters = StringField('Letters', validators=[DataRequired()])
    submit = SubmitField('Submit')


