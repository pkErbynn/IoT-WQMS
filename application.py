from flask import Flask, render_template
from aquaLite import read_data_from_db
import datetime
# from sample import read_data_from_db
app = Flask(__name__)


@app.route("/")
def index():
    items = read_data_from_db()
    # items = read_data_from_db()
    # month = timedate.timedate.now().month
    # day = timedate.timedate.now().day
    # hour = timedate.timedate.now().hour
    return render_template("index.html", todayDate=datetime.date.today(), items=items)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


#  https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js
