from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"Book {self.title}"


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    query = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = query.scalars().all()
    book_count = len(all_books)
    return render_template('index.html', books=all_books, book_count=book_count)


@app.get("/add")
def add():
    return render_template('add.html')


@app.post("/add")
def post_book():
    with app.app_context():
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
    return redirect(url_for('home'))


@app.get("/edit/<int:book_id>")
def edit(book_id):
    book = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book, id=book_id)


@app.post("/edit/<int:book_id>")
def edit_book(book_id):
    with app.app_context():
        book = db.get_or_404(Book, book_id)
        book.title = request.form["title"] if request.form["title"] != "" else book.title
        book.author = request.form["author"] if request.form["author"] != "" else book.author
        book.rating = request.form["rating"] if request.form["rating"] != "" else book.rating
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
