from flask import Flask, render_template, flash, redirect, render_template, request, session, abort
from aquaLite import read_data_from_db
import datetime
# from sample import read_data_from_db
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    if request.authorization and request.authorization.username=="username" and request.authorization.password=="password":
        return render_template("dashboard.html")
    return render_template("index.html")
# def index():
#     items = read_data_from_db()
#     # items = read_data_from_db()
#     # month = timedate.timedate.now().month
#     # day = timedate.timedate.now().day
#     # hour = timedate.timedate.now().hour
#     return render_template("index.html", todayDate=datetime.date.today(), items=items)


# @app.route("/dashboard.html", methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return render_template("dashboard.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


