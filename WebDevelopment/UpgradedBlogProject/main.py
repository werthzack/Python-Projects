import werkzeug.exceptions
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_ckeditor import CKEditor
from form import NewPostForm
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    query = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    all_posts = query.scalars().all()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:post_id>', methods=["GET"])
def show_post(post_id):
    try:
        requested_post = db.get_or_404(BlogPost, post_id)
        return render_template("post.html", post=requested_post)
    except werkzeug.exceptions.NotFound:
        return "The requested post was not found"


@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    post_form = NewPostForm()
    if post_form.validate_on_submit():
        new_blog = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.sub_title.data,
            date=date.today().strftime("%B %d, %Y"),
            body=post_form.body.data,
            author=post_form.author.data,
            img_url=post_form.image_url.data
        )
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, method="New")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_blog(post_id):
    try:
        requested_post = db.get_or_404(BlogPost, post_id)
    except werkzeug.exceptions.NotFound:
        return "The requested requested_post was not found"

    post_form = NewPostForm(
        title=requested_post.title,
        sub_title=requested_post.subtitle,
        image_url=requested_post.img_url,
        author=requested_post.author,
        body=requested_post.body
    )

    if post_form.validate_on_submit():
        requested_post.title = post_form.title.data
        requested_post.subtitle = post_form.sub_title.data
        requested_post.img_url = post_form.image_url.data
        requested_post.author = post_form.author.data
        requested_post.body = post_form.body.data

        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=post_form, method="Edit")


@app.route("/delete-post/<int:post_id>")
def delete_blog(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(requested_post)
    db.session.commit()

    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
