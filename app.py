from flask import Flask, render_template, request
from music import recommender, checker, lister

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/music", methods = ["POST", "GET"])
def music():
    if request.method == "POST":
        m = request.form["input"]
       
        if checker(m) == "1":
            n,g,r,p = recommender(m)
            boom = 100
            return render_template("music.html", n=n,g=g,r=r,p=p,boom=boom)
        else:
            boom = 420
            return render_template("music.html", boom=boom)
    return render_template("music.html")

@app.route("/list")
def list():
    n,g,r,p = lister()
    return render_template("list.html", n=n, g=g, r=r, p=p)


if __name__ == "__main__":
    app.run(debug=True)