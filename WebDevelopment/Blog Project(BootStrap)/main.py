from flask import Flask, render_template, url_for, request
import requests
import smtplib
import webbrowser

app = Flask(__name__)


def send_mail(name, email, number, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="@gmail.com", password="password")
        connection.sendmail(
            from_addr="theabiolasmail@gmail.com",
            to_addrs="timmyabiola27@gmail.com",
            msg=f"Name: {name}"
                f"Number: {number}"
                f"Body: {message}"
        )


@app.route("/")
def home():
    blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("index.html", data=blog_data.json())


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def get_blog_page(blog_id: int):
    blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    for blog in blog_data:
        if blog["id"] == blog_id:
            return render_template("post.html", data=blog)


@app.post("/contact")
def send_details():
    send_mail(request.form["name"], request.form["email"], request.form["phone"], request.form["message"])
    return app.redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
