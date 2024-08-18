import sqlalchemy.exc
import werkzeug.exceptions
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=to_dict(random_cafe))


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])


@app.route("/find")
def find_cafe():
    cafe_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(cafe_location == Cafe.location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("location"),
        seats=request.args.get("seats"),
        has_toilet=request.args.get("has_toilet"),
        has_wifi=request.args.get("has_wifi"),
        has_sockets=request.args.get("has_sockets"),
        can_take_calls=request.args.get("can_take_calls"),
        coffee_price=request.args.get("coffee_price")
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(success="Successfully added the new Cafe")
    except sqlalchemy.exc.IntegrityError as error:
        error_message = str(error)
        if "NOT NULL constraint failed" in error_message:
            field_name = error_message.split(":")[1].split("\n")[0].strip()
            print(field_name)
            return jsonify({
                "error": "IntegrityError",
                "message": f"The field '{field_name}' cannot be null. Please provide a value for '{field_name}'."
            }), 400


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    except werkzeug.exceptions.NotFound:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        db.session.delete(cafe)
        db.session.commit()
        if api_key == "password":
            return jsonify(status="Api Key Accepted"), 200
        else:
            return jsonify(status="Invalid Api Key")
    except werkzeug.exceptions.NotFound:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
