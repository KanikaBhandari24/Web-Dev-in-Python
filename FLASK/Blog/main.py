from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
email=""
pas=""

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        data=request.form
        print(data["username"])
        print(data["mail"])
        print(data["hone"])
        print(data["msg"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send(name, email, phone, message):
    email_msg=f"Subject: New msg\n\nName:{name}\nEmail: {email}\n Phone:{phone}\n, Message:{message}"
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(email, pas)
        con.sendmail(email, email, email_msg) 

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
