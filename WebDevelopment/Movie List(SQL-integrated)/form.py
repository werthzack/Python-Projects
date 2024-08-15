from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class MovieEditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g 7.5")
    review = StringField("Review")
    submit = SubmitField("Update")


class MovieCreateForm(FlaskForm):
    title = StringField("Movie Title", [DataRequired()])
    submit = SubmitField("Search Movie")
