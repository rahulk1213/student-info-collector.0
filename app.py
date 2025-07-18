from flask import Flask , request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/info", methods = ["POST", "GET"])
def info():
    if request.method == "POST":
        name = request.form.get("name")
        roll_no = request.form.get("roll_no")
        collage = request.form.get("collage")
        branch = request.form.get("branch")

        return render_template("info.html", name = name, roll_no = roll_no , collage = collage ,branch = branch )

    return render_template("home.html")         
    


if __name__ == "__main__":
    app.run(debug=True)
