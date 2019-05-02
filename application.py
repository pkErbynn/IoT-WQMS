'''
Water Quality System (WQMS) 

Created : March 2019

Authors : John Pk Erbynn, Josiah, Isaac Agyen

'''



from flask import Flask, render_template, flash, redirect, render_template, request, session, abort
from aquaLite import *
from flask import jsonify
import datetime
import json
import sqlite3
import time
import statistics as stat
app = Flask(__name__)



# home route

@app.route("/",)
@app.route("/index")
def index():
#     # if request.phization and request.phization.username=="username" and request.phization.password=="password":
#     #     return render_template("dashboard.html")
#     # return render_template("index.html")
#      items = read_data_from_db()
#     # items = read_data_from_db()
#    
    # return render_template("index.html", todayDate=datetime.date.today(), items=items)
    
    return render_template("index.html", todayDate=datetime.date.today())


# posting data to database

@app.route("/postData", methods=["POST"])
def create_data():
    # data format 01 not accepted
    data = request.get_json()
    # data = request.data
    print(".......")
    print(data)
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    print("temperature:", data['temperature'])

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



# empty list to be used for all parameter route
time = []
ph=[]
temp= []
turbidity= []
waterlevel=[]

# initial temps
average_temp = 0
min_temp=0
max_temp=0
range_temp = 0

@app.route("/tempChart/<x>")
def temperature(x):

    # connecting to datebase
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    #  depending on time interval for pushing data from sensor to database, that the limit of data to be determined  
    
    # data processing for an hour

    if x == '1h':
        name = '1 Hour'
        label = 'Minute'
    
        cursor.execute(" SELECT time,temperature FROM ( SELECT * from iot_wqms_table ORDER BY id DESC LIMIT 120 ) order by id asc ") 
        data = cursor.fetchall()

        for d in data:
            print(d)
        
        # emptying list 
        del time[:]
        del temp[:]
    
        for datum in data:
            print(datum)
            datum_float = float(datum[1])
            temp.append(datum_float)
            t = str(datum[0][14:])
            time.append(t)
        
        print("time...." , time)
        print("temp....", temp)
        print("lenght : ", len(temp))

        # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp



    # data processing for a day
    
    if x == '1d':
        name = '1 Day'
        label = 'Hour'
    
        cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id ASC LIMIT 2880 ") 
        data = cursor.fetchall()

        del time[:] # time on the x-axis
        del temp[:]
    
        for datum in data:
            print(datum)
            datum_float = float(datum[1])
            temp.append(datum_float)
            t = str(datum[0][11:16])
            time.append(t)
        
        print("time...." , time)
        print("temp....", temp)
        print("length : ",len(temp))

        # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp




    # weekly data processing ,,,,,

    if x == '1w':
        name = '1 Week'
        label = 'Day'

        # fetching data from database
        cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id ASC LIMIT 20160") 
        data = cursor.fetchall()
        
        # converting timestamp from database to day in string like Mon, Tue
        def date_to_day(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%a"))

        # emptying time and temperature container list
        del time[:]
        del temp[:]

        # retrieving weekly time and temp from database data
        for datum in data:
            # collecting temperature
            print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list

            # string day processing from full timestamp
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])

            # using full_date to day_string function defined 
            current_day = date_to_day(year, month, day)
            time.append(current_day)
            
        
        print("time...." , time)
        print("temp....", temp)

        # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp



    # monthly data processing

    if x == '1m':
        name = '1 Month'
        label = 'Month-Date'

        # fetching data from database.....change number of data to fetch
        cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id ASC LIMIT 87600") 
        data = cursor.fetchall()
        
        # retreiving month string from timestamp of database to get sth like January, Febuary
        def string_month_from_full_date(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%b")) # %B for fullname

        # emptying time and temperature container list
        del time[:]
        del temp[:]

        # retrieving monthly time and temp from database data
        for datum in data:
            # collecting temperature
            print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list

            # string month processing from full date timestamp
            tm = str(datum[0][5:10])
            # tm_split = tm.split("-")
            # year = int(tm_split[0])
            # month = int(tm_split[1])
            # day = int(tm_split[2])

            # using full_date to day_string function defined 
            # current_month = string_month_from_full_date(year, month, day)
            # time.append(current_month)
            time.append(tm)
            
        
        print("time...." , time)
        print("temp....", temp)

         # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp




    # yearly data processing

    if x == '1y':
        name = '1 Year'
        label = 'Month'

        # fetching data from database.....change number of data to fetch
        cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id ASC LIMIT 1051333") 
        data = cursor.fetchall()
        
         # retreiving month string from timestamp of database to get sth like January, Febuary
        def string_month_from_full_date(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%b")) # %B for fullname


        # emptying time and temperature container list
        del time[:]
        del temp[:]

        # retrieving monthly time and temp from database data
        for datum in data:
            # collecting temperature
            print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list

            # string month processing from full date timestamp
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])

            # using full_date to day_string function defined 
            current_month = string_month_from_full_date(year, month, day)
            time.append(current_month)
            # time.append(year)
            
        print("time...." , time)
        print("temp....", temp)

         # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp



    # all data processing

    if x == 'all':
        name = 'All'
        label = 'Year-Month'

        # fetching data from database.....change number of data to fetch
        # cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id DESC LIMIT 1440") 
        cursor.execute(" SELECT time,temperature FROM ( SELECT * from iot_wqms_table ORDER BY id DESC ) order by id asc") 
        
        data = cursor.fetchall()
        
        #  # retreiving month string from timestamp of database to get sth like January, Febuary
        # def string_month_from_full_date(year, month, day):
        #     time = datetime.datetime(year, month, day)
        #     return (time.strftime("%Y")) # %B for fullname


        # emptying time and temperature container list
        del time[:]
        del temp[:]

        # retrieving monthly time and temp from database data
        for datum in data:
            # collecting temperature
            print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list

            # string month processing from full date timestamp
            tm = str(datum[0][:7])
            # tm_split = tm.split("-")
            # year = int(tm_split[0])
            # month = int(tm_split[1])
            # day = int(tm_split[2])

            # using full_date to day_string function defined 
            # current_month = string_month_from_full_date(year, month, day)
            # time.append(current_month)
            time.append(tm)
            
        print("time...." , time)
        print("temp....", temp)

         # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)

        min_temp = round(min(temp), 2) # assigned to global min_temp

        max_temp = round(max(temp), 2)

        range_temp = max_temp - min_temp


    return render_template("tempChart.html", temp=temp, time=time, label=label, name=name, mean=average_temp, max_temp=max_temp, min_temp=min_temp, range_temp=range_temp)


@app.route("/phChart")
def ph():
    return render_template("phChart.html")


@app.route("/turbChart")
def turb():
    return render_template("turbChart.html")


@app.route("/waterlevelChart")
def waterlevel():
    return render_template("waterlevelChart.html")



@app.route("/dashboard", methods=["GET"])
def dashboard():
    # items = read5_data_from_db()
    # return render_template("dashboard.html", data=items)
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    cursor.execute(" SELECT * FROM iot_wqms_table ORDER BY id DESC LIMIT 120") 
    data = cursor.fetchall()
    data = list(data)
    print("data.....", data)

    # mean temperature
    temp_data = []  # collecting temp values

    for row in data:
        temp_data.append(row[2])    # getting temperature values

    mean_temp = stat.mean(temp_data)  # calc mean temperature value
    average_temp = round(mean_temp, 2)  # mean temperature value in 2 decimal places

    # last value data
    last_temp_data = temp_data[0]

    print('current temp', last_temp_data)


    # percentage increase for temperature computation

    # current current sum
    current_hour_sum = round(sum(temp_data), 2)
    print("sum...", current_hour_sum)
    
    # prev 120 sum....last but one 120 data
    cursor.execute(" SELECT * FROM iot_wqms_table ORDER BY id DESC LIMIT 240") 
    data = list(cursor.fetchall())

    prev_temp_data = []  # collecting temp values

    for row in data:
        prev_temp_data.append(row[2])
    
    prev_temp_data = prev_temp_data[-240:-120]
    prev_hour_sum = sum(prev_temp_data)
    
    # now, getting the percentage change
    temp_change = prev_hour_sum - current_hour_sum
    temp_change = round(temp_change, 2)
    percentage_temp_change = (temp_change/current_hour_sum) * 100
    percentage_temp_change = round(percentage_temp_change,1)


    return render_template("dashboard.html", data=data, average_temp_hour=average_temp, percentage_temp_change=percentage_temp_change, temp_change=temp_change, last_temp_data = last_temp_data)


if __name__ == "__main__":
    app.debug = True
    # app.run()   # using default local ip

    app.run(debug=True, host='10.10.65.22', port=5050)   # setting your own ip
