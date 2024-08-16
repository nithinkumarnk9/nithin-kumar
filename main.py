from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/About")
def About():
    return render_template("About.html")
@app.route("/Contact")
def Contact():
    return render_template("Contact.html")
@app.route("/card1")
def card1():
    return render_template("card1.html")
@app.route("/card2")
def card2():
    return render_template("card2.html")
@app.route("/card3")
def card3():
    return render_template("card3.html")
@app.route("/card4")
def card4():
    return render_template("card4.html")
@app.route("/card5")
def card5():
    return render_template("card5.html")
@app.route("/card6")
def card6():
    return render_template("card6.html")

if __name__ == '__main__':
     app.run(debug=True)