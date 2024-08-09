from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


emojis = {
    "coffee": "☕️",
    "wifi": "💪",
    "power": "🔌"
}


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = URLField('Location URL', validators=[DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    choices = {
        "coffee": [],
        "wifi": [],
        "power": []
    }
    for i in range(6):
        print(i)
        for a, key in enumerate(choices):
            emoji = emojis[key] if i > 0 else "✘"
            print(emoji)
            choices[key].append((i, "✘" if i < 1 else emojis[key] * i))

    print(choices["coffee"])
    coffee_rating = SelectField('Coffee Rating', choices=choices["coffee"], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=choices["wifi"], validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating', choices=choices["power"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
@app.route("/")
# ---------------------------------------------------------------------------


# all Flask routes below
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    new_form = CafeForm()
    if new_form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()home

    return render_template('add.html', form=new_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
