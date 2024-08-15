import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

from form import MovieEditForm, MovieCreateForm
from movieSearch import MovieSearch
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    review: Mapped[float] = mapped_column(Integer, nullable=True)
    image_url: Mapped[str] = mapped_column(String(250))

    def __repr__(self):
        return f"Movie {self.title}"


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    query = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = query.scalars().all()[::-1]
    movie_count = len(all_movies)
    return render_template("index.html", movies=all_movies, count=movie_count)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    movie_form = MovieEditForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if movie_form.validate_on_submit():
        movie.rating = request.form.get("rating") if request.form.get("rating") != "" else movie.rating
        movie.review = request.form.get("review") if request.form.get("review") != "" else movie.review
        db.session.commit()
        return app.redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=movie_form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()

    return app.redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    movie_form = MovieCreateForm()
    if movie_form.validate_on_submit():
        title = request.form["title"]
        params = searchManager.search_movie(title)
        return render_template("select.html", movies=params)
    return render_template('add.html', form=movie_form)


@app.route("/submit")
def submit_movie():
    movie_id = request.args.get("movie_id")
    selected_movie = searchManager.get_movie(movie_id)
    movie = Movie(
        title=selected_movie["title"],
        year=dt.strptime(selected_movie["release_date"], "%Y-%m-%d").year,
        description=selected_movie["overview"],
        image_url=f"https://image.tmdb.org/t/p/w500/{selected_movie["poster_path"]}"
    )
    db.session.add(movie)
    db.session.commit()
    return app.redirect(url_for('edit_movie', id=movie.id))


if __name__ == '__main__':
    searchManager = MovieSearch()
    app.run(debug=True)
