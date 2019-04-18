from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():   
    return render_template('index.html')   
    # return "Hello Boss!  <a href='/logout'>Logout</a>"

time = []
temp=[]
moist = []
humidity=[]


@app.route('/atmtemp/<x>')
def atmtemp(x):
    if x == '1h':
        name = '1 HOUR'
        label = 'Minutes'
        with open('./readings/atmp1h.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 HOUR'
        label = 'Hours'
        with open('./reading.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 WEEK'
        label = 'Days'
        with open('./reaading2.embs'    ) as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 MONTH'
        label = 'Weeks'
        with open('./reaading2.embs'    ) as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 YEAR'
        label = 'Months'
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('atm_temp.html', temp=temp, time=str(time), name=name, label=label)




@app.route('/soiltemp/<x>')
def soiltemp(x):
    if x == '1h':
        name = '1 HOUR'
        label = 'Minutes'
        with open('./readings/stmp1h.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 HOUR'
        label = 'Hours'
        with open('./reading.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 WEEK'
        label = 'Days'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 MONTH'
        label = 'Weeks'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 YEAR'
        label = 'Months'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_temp.html', temp=temp, time=str(time), name=name, label=label)

@app.route('/soilmoist/<x>')
def soilmoist(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        with open('./reading.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                moist.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_moist.html', moist=moist, time=str(time))


@app.route('/humidity/<x>')
def humid(x):
    if x == '1h':
        name =  '1 Hour'
        label = 'Minutes'
        with open('./readings/humidity1h.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 Hour'
        label = 'Hours'
        with open('./reading.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 Week'
        label = 'Days'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 Month'
        label = 'Weeks'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 Year'
        label = 'Months'
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('humidity.html', humidity=humidity, time=str(time), name=name, label=label)


if __name__ == '__main__':
    app.run(debug=True,)
