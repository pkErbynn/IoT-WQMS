from flask import Flask, render_template
# from sqlite import get_values
from sample import read_data_from_db
app = Flask(__name__)


@app.route("/")
def index():
    # items = get_values()
    # [(23, '2018-11-02 19:52:31', 24.0, 50.0, 45.3, 40.3), (24, '2018-11-02 19:52:31', 35.0, 44.0, 25.0, 40.0)]
    items = read_data_from_db()
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


#  https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js