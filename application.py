from flask import Flask, render_template, flash, redirect, render_template, request, session, abort
from aquaLite import *
from flask import jsonify
import datetime
import json
import sqlite3
import time
# from sample import read_data_from_db
app = Flask(__name__)


@app.route("/",)
@app.route("/index")
def index():
#     # if request.phization and request.phization.username=="username" and request.phization.password=="password":
#     #     return render_template("dashboard.html")
#     # return render_template("index.html")
#      items = read_data_from_db()
#     # items = read_data_from_db()
#     # month = timedate.timedate.now().month
#     # day = timedate.timedate.now().day
#     # hour = timedate.timedate.now().hour
    # return render_template("index.html", todayDate=datetime.date.today(), items=items)
    return render_template("index.html", todayDate=datetime.date.today())



@app.route("/postData", methods=["POST"])
def add_row_data():
    data = request.get_json()
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    # print("temperature:", data['temperature'])

    cursor.execute(""" INSERT INTO iot_wqms_table( temperature, turbidity, ph, water_level) 
                       VALUES (?, ?, ?, ?) """,
                   (data["temperature"], data["turbidity"], data["ph"], data["water_level"]))
    con.commit()
    return jsonify({ "Status": "Data posted successfully"})



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
    # items = read5_data_from_db()
    # return render_template("dashboard.html", data=items)
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
    # app.run(debug=True, host='10.10.64.90', port=5050)


