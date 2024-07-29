from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("index.html", data=blog_data.json())


@app.route('/post/<int:blog_id>')
def get_blog_page(blog_id: int):
    blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    for blog in blog_data:
        if blog["id"] == blog_id:
            return render_template("post.html", data=blog)


if __name__ == "__main__":
    app.run(debug=True)
