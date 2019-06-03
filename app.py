'''
Water Quality System (WQMS) 

This module is the bussiness logic layer. 
It does data validation,
...dynamic data processing,
...generates and render contents to be delivered to UI 
...pulls data from DB for processing
...data download in csv format

Usage:
    run <python app.py> 
    follow url given

Created : March 2019

Author(s) : John Pk Erbynn(john.erbynn@gmail.com), 
            Josiah Nii Kortey(josiahkotey13@gmail.com), 
            Isaac Agyen Duffour(izagyen96@gmail.com)

'''


from flask import Flask, render_template, flash, redirect, request, jsonify, url_for, Response
# from aquaLite import *
import datetime
import json
import sqlite3
import time
import statistics as stat
import mail
from config import credential
import generator
from flask_toastr import Toastr     # toastr module import
import create_database


app = Flask(__name__)

# python notification toaster
toastr = Toastr(app)

# Set the secret_key on the application to something unique and secret.
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


# home route....landing page
@app.route("/", methods = ['GET', 'POST'])
@app.route("/index", methods=["GET", "POST"])
def index():
    print("landing page running...")
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']

        # credentials from config files imported
        if username == credential['name'] and passwd == credential['passwd']:
            flash('Login successful :)', 'success')
            # flash("You have successfully logged in.", 'success')    # python Toastr uses flash to flash pages
            return redirect(url_for('dashboard')) 
        else:
            flash('Login Unsuccessful. Please check username and password', 'error')

    return render_template("index.html", todayDate=datetime.date.today(), )


# posting collected data to database
@app.route("/postData", methods=["POST"])
def create_data():

    """
    To remotely access this route and post data after deployment on Heroku, use:
        <deployed link>/postData
        Eg; https://wqms.herokuapp.com/postData
    """

    print(">>> posting data ....")
    # expected data format from microcontroller;
    # b"temperatureValue", "turbidityValue", "phValue", "waterlevelValue"
    # data = request.data

    # # decoding bytes data to string
    # decoded_data = data.decode('utf-8')  
    # key = ['temperature', 'turbidity', 'ph', 'water_level']

    # # data into list
    # string_value = decoded_data.split(',')

    # # dictionary processing
    # value = []
    # for v in string_value:
    #     v = float(v)
    #     value.append(v)

    # #merge to dict()
    # data = dict(zip(key, value))
    # # print(data)


    """
    for testing purposes with Postman(json data format), use:
        request.json and comment code above to line 79(data.request)
    """
    data = request.json
    print(data)


    """
    This code snippet handles database posting
    """
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    print('before try...')
    try:
        cursor.execute(""" INSERT INTO iot_wqms_table( temperature, turbidity, ph, water_level) 
                         VALUES (?, ?, ?, ?) """,
                   (data["temperature"], data["turbidity"], data["ph"], data["water_level"]))
        con.commit()
        print("Data posted SUCCESSFULLY")
    except Exception as err:
        print('...posting data FAILED')
        print(err)


    """
    This attribute sends an email as an alert whenever data is out of normal range
    normal parameter ranges ;
        ...temp 23-34
        ...turbidity(Nephelometric Turbidity Units or Jackson Turbidity Unit) 0 - 5
        ...ph   4-10
        ...water level 5 - 27

    example;
            {'temperature': 25.31, 'turbidity': 4.13, 'ph': 8.04, 'water_level': 16.0}
    """

    try:
        if (data["temperature"] < 23) | (data["temperature"] > 34) | \
            (data["turbidity"] < 0) | (data["turbidity"] > 5) | \
                (data["ph"] < 6) | (data["ph"] > 10) | \
                    (data["water_level"] < 5) | (data["water_level"] > 27) :
            mail.send_mail(data)
          
    except Exception as err:
        print(f'Email unsuccessful. {err}')
    
   
    return jsonify({ "Status": "Data posted successfully\n"})


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
    print(">>> temperature page running ...")
    # connecting to datebase
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    #  30secs time interval for pushing data from sensor to database, that the limit of data to be determined  
    
    # data processing for an hour 
    if x == '1h':
        name = '1 Hour'
        label = 'Minute'

        # with 30 seconds interval, ...2,880 temperature data will be posted within an hour
        cursor.execute(" SELECT time,temperature FROM ( SELECT * from iot_wqms_table ORDER BY id DESC LIMIT 120 ) order by id asc ") 
        data = cursor.fetchall()
        
        # emptying list 
        del time[:]
        del temp[:]
    
        for datum in data:
            # temperature data extraction
            datum_float = float(datum[1])
            temp.append(datum_float)
            # time extraction
            t = str(datum[0][14:])
            time.append(t)
        
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
            # print(datum)
            datum_float = float(datum[1])
            temp.append(datum_float)
            t = str(datum[0][11:16])
            time.append(t)
        
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
            # print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list

            # string month processing from full date timestamp
            tm = str(datum[0][5:10])
            time.append(tm)

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
            # print(datum)
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
            
         # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)
        min_temp = round(min(temp), 2) # assigned to global min_temp
        max_temp = round(max(temp), 2)
        range_temp = max_temp - min_temp


    # all data processing

    if x == 'all':
        name = 'All'
        label = 'Time'

        # fetching data from database.....change number of data to fetch
        # cursor.execute(" SELECT time,temperature FROM iot_wqms_table ORDER BY id DESC LIMIT 1440") 
        cursor.execute(" SELECT time,temperature FROM ( SELECT * from iot_wqms_table ORDER BY id DESC ) order by id asc") 
        data = cursor.fetchall()

        # emptying time and temperature container list
        del time[:]
        del temp[:]

        # retrieving monthly time and temp from database data
        for datum in data:
            # collecting temperature
            # print(datum)
            datum_float = float(datum[1])   # temp data in float
            temp.append(datum_float)        # pushing to temp list
            # string month processing from full date timestamp
            tm = str(datum[0][:7])
            time.append(tm)
            
         # analysis
        mean_temp = stat.mean(temp)
        average_temp = round(mean_temp, 2)
        min_temp = round(min(temp), 2) # assigned to global min_temp
        max_temp = round(max(temp), 2)
        range_temp = max_temp - min_temp

    return render_template("tempChart.html", temp=temp, time=time, label=label, name=name, mean=average_temp, max_temp=max_temp, min_temp=min_temp, range_temp=range_temp)


@app.route("/phChart/<x>")
def powerOfHydrogen(x):
    print(">>> ph page running ...")
    # connecting to datebase
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    # data processing for an hour 
    if x == '1h':
        name = '1 Hour'
        label = 'Minute'

        # selecting ph data
        cursor.execute(" SELECT time, ph FROM ( SELECT * from iot_wqms_table ORDER BY id DESC LIMIT 120 ) order by id asc ") 
        data = cursor.fetchall()
        # print(data)

        # emptying list 
        del time[:]
        del ph[:]

        # data extraction
        for datum in data:
            # print(datum)
            # extracting ph data
            datum_float = float(datum[1])
            ph.append(datum_float)
            # extracting minutes and seconds
            t = str(datum[0][14:])
            time.append(t)
        
        # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )

    # data processing for day 
    if x == '1d':
        name = '1 Day'
        label = 'Hour'

        # selecting ph data
        cursor.execute(" SELECT time, ph FROM iot_wqms_table ORDER BY id ASC LIMIT 2880 ") 
        data = cursor.fetchall()

        # emptying list 
        del time[:]
        del ph[:]

        # data extraction
        for datum in data:
            # print(datum)
            # extracting ph data
            datum_float = float(datum[1])
            ph.append(datum_float)
            # extracting minutes and seconds
            t = str(datum[0][11:16])
            time.append(t)

        # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )


     # weekly data processing ,,,,,

    if x == '1w':
        name = '1 Week'
        label = 'Day'

        # fetching data from database
        cursor.execute(" SELECT time, ph FROM iot_wqms_table ORDER BY id ASC LIMIT 20160") 
        data = cursor.fetchall()
        
        # converting timestamp from database to day in string like Mon, Tue
        def date_to_day(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%a"))

        # emptying time and ph container list
        del time[:]
        del ph[:]

        # retrieving weekly time and ph from database data
        for datum in data:
            # collecting ph
            # print(datum)
            datum_float = float(datum[1])   # ph data in float
            ph.append(datum_float)        # pushing to ph list

            # string day processing from full timestamp
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])

            # converting full_date to day_string function defined 
            current_day = date_to_day(year, month, day)
            time.append(current_day)
            
        # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )

    
     # monthly data processing

    if x == '1m':
        name = '1 Month'
        label = 'Month-Date'

        # fetching data from database.....change number of data to fetch
        cursor.execute(" SELECT time, ph FROM iot_wqms_table ORDER BY id ASC LIMIT 87600") 
        data = cursor.fetchall()

        # emptying list
        del time[:]
        del ph[:]

        # extracting monthly time and ph data to empty list
        for datum in data:
            # collecting ph
            # print(datum)
            datum_float = float(datum[1])   # ph data to float
            ph.append(datum_float)       

            # extracting month from full timestamp
            tm = str(datum[0][5:10])
            time.append(tm)
        
         # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )


    # yearly data processing

    if x == '1y':
        name = '1 Year'
        label = 'Month'

        cursor.execute(" SELECT time, ph FROM iot_wqms_table ORDER BY id ASC LIMIT 1051333") 
        data = cursor.fetchall()

         # retreiving month in string from timestamp of database to get sth like January, Febuary
        def string_month_from_full_date(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%b")) # %B for fullname

        # emptying
        del time[:]
        del ph[:]

        # retrieving monthly time and ph to emptied list above
        for datum in data:
            # collecting ph
            datum_float = float(datum[1])   # temp data in float
            ph.append(datum_float)        # pushing to temp list

            # string month processing from full date timestamp
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])

            # using full_date to day_string function to get month in string 
            current_month = string_month_from_full_date(year, month, day)
            time.append(current_month)

        # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )

    
    # all data processing

    if x == 'all':
        name = 'All'
        label = "Time"
        cursor.execute(" SELECT time, ph FROM ( SELECT * from iot_wqms_table ORDER BY id DESC ) order by id asc") 
        data = cursor.fetchall()
        
        # emptying 
        del time[:]
        del ph[:]
        # retrieving monthly time and ph to emptied list
        for datum in data:
            # collecting temperature
            datum_float = float(datum[1])   # ph data in float
            ph.append(datum_float)        # pushing to ph list

            # string month processing from full date timestamp
            tm = str(datum[0][:7])
            time.append(tm)
            
        # analysis
        average_ph = round(stat.mean(ph), 2)
        min_ph = round(min(ph), 2)
        max_ph = round(max(ph), 2)
        range_ph = float( round((max_ph - min_ph), 2) )

    return render_template("phChart.html", ph=ph, time=time, label=label, name=name, average_ph=average_ph, min_ph=min_ph, max_ph=max_ph, range_ph=range_ph)


@app.route("/turbChart/<x>")
def turb(x):
    print(">>> turbidity page running ...")
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()
    if x == '1h':
        name = '1 Hour'
        label = 'Minute'
        cursor.execute(" SELECT time, turbidity FROM ( SELECT * from iot_wqms_table ORDER BY id DESC LIMIT 120 ) order by id asc ") 
        data = cursor.fetchall()
        del time[:]
        del turbidity[:]
        for datum in data:
            datum_float = float(datum[1])
            turbidity.append(datum_float)
            t = str(datum[0][14:])
            time.append(t)
        average_turbidity = round(stat.mean(turbidity), 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )
        print("range", range_turbidity)
    
    # data processing for day 
    if x == '1d':
        name = '1 Day'
        label = 'Hour'
        cursor.execute(" SELECT time, turbidity FROM iot_wqms_table ORDER BY id ASC LIMIT 2880 ") 
        data = cursor.fetchall()
        del time[:]
        del turbidity[:]
        # appending data to emptied list
        for datum in data:
            datum_float = float(datum[1])
            turbidity.append(datum_float)
            t = str(datum[0][11:16])
            time.append(t)
        # to 2 decimal places
        average_turbidity = round( stat.mean(turbidity) , 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )

    if x == '1w':
        name = '1 Week'
        label = 'Day'
        cursor.execute(" SELECT time, turbidity FROM iot_wqms_table ORDER BY id ASC LIMIT 20160") 
        data = cursor.fetchall()
        def date_to_day(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%a"))
        del time[:]
        del turbidity[:]
        for datum in data:
            # print(datum)
            datum_float = float(datum[1])   # ph data in float
            turbidity.append(datum_float)        # pushing to ph list
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])
            current_day = date_to_day(year, month, day)
            time.append(current_day)
        average_turbidity = round( stat.mean(turbidity) , 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )

    if x == '1m':
        name = '1 Month'
        label = 'Month-Date'
        cursor.execute(" SELECT time, turbidity FROM iot_wqms_table ORDER BY id ASC LIMIT 87600") 
        data = cursor.fetchall()
        del time[:]
        del turbidity[:]
        for datum in data:
            datum_float = float(datum[1])   # ph data to float
            turbidity.append(datum_float)       
            tm = str(datum[0][5:10])
            time.append(tm)
        average_turbidity = round( stat.mean(turbidity) , 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )
    
    if x == '1y':
        name = '1 Year'
        label = 'Month'
        cursor.execute(" SELECT time, turbidity FROM iot_wqms_table ORDER BY id ASC LIMIT 1051333") 
        data = cursor.fetchall()
        def string_month_from_full_date(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%b")) # %B for fullname
        del time[:]
        del turbidity[:]
        for datum in data:
            datum_float = float(datum[1])   # temp data in float
            turbidity.append(datum_float)        # pushing to temp list
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])
            current_month = string_month_from_full_date(year, month, day)
            time.append(current_month)
        average_turbidity = round( stat.mean(turbidity) , 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )

    if x == 'all':
        name = 'All'
        label = "Time"
        cursor.execute(" SELECT time, turbidity FROM ( SELECT * from iot_wqms_table ORDER BY id DESC ) order by id asc") 
        data = cursor.fetchall()
        del time[:]
        del turbidity[:]
        for datum in data:
            datum_float = float(datum[1])   # ph data in float
            turbidity.append(datum_float)        # pushing to ph list
            tm = str(datum[0][:7])
            time.append(tm)
        average_turbidity = round( stat.mean(turbidity) , 2)
        min_turbidity = round(min(turbidity), 2)
        max_turbidity = round(max(turbidity), 2)
        range_turbidity = float( round((max_turbidity - min_turbidity), 2) )

    return render_template("turbChart.html", turbidity=turbidity, time=time, label=label, name=name, average_turbidity=average_turbidity, min_turbidity=min_turbidity, max_turbidity=max_turbidity, range_turbidity=range_turbidity)


@app.route("/waterlevelChart/<x>")
def waterdepth(x):
    print(">>> waterlevel page running ...")
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()
    if x == '1h':
        name = '1 Hour'
        label = 'Minute'
        cursor.execute(" SELECT time, water_level FROM ( SELECT * from iot_wqms_table ORDER BY id DESC LIMIT 120 ) order by id asc ") 
        data = cursor.fetchall()
        del time[:]
        del waterlevel[:]
        for datum in data:
            datum_float = float(datum[1])
            waterlevel.append(datum_float)
            t = str(datum[0][14:])
            time.append(t)
        average_waterlevel = round(stat.mean(waterlevel), 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )
    
    # data processing for day 
    if x == '1d':
        name = '1 Day'
        label = 'Hour'
        cursor.execute(" SELECT time, water_level FROM iot_wqms_table ORDER BY id ASC LIMIT 2880 ") 
        data = cursor.fetchall()
        del time[:]
        del waterlevel[:]
        for datum in data:
            datum_float = float(datum[1])
            waterlevel.append(datum_float)
            t = str(datum[0][11:16])
            time.append(t)
        average_waterlevel = round( stat.mean(waterlevel) , 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )

    if x == '1w':
        name = '1 Week'
        label = 'Day'
        cursor.execute(" SELECT time, water_level FROM iot_wqms_table ORDER BY id ASC LIMIT 20160") 
        data = cursor.fetchall()
        def date_to_day(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%a"))
        del time[:]
        del waterlevel[:]
        for datum in data:
            # print(datum)
            datum_float = float(datum[1])   # ph data in float
            waterlevel.append(datum_float)        # pushing to ph list
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])
            current_day = date_to_day(year, month, day)
            time.append(current_day)
        average_waterlevel = round( stat.mean(waterlevel) , 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )

    if x == '1m':
        name = '1 Month'
        label = 'Month-Date'
        cursor.execute(" SELECT time, water_level FROM iot_wqms_table ORDER BY id ASC LIMIT 87600") 
        data = cursor.fetchall()
        del time[:]
        del waterlevel[:]
        for datum in data:
            datum_float = float(datum[1])   # ph data to float
            waterlevel.append(datum_float)       
            tm = str(datum[0][5:10])
            time.append(tm)
        average_waterlevel = round( stat.mean(waterlevel) , 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )
    
    if x == '1y':
        name = '1 Year'
        label = 'Month'
        cursor.execute(" SELECT time, water_level FROM iot_wqms_table ORDER BY id ASC LIMIT 1051333") 
        data = cursor.fetchall()
        def string_month_from_full_date(year, month, day):
            time = datetime.datetime(year, month, day)
            return (time.strftime("%b")) # %B for fullname
        del time[:]
        del waterlevel[:]
        for datum in data:
            datum_float = float(datum[1])   # temp data in float
            waterlevel.append(datum_float)        # pushing to temp list
            tm = str(datum[0][:10])
            tm_split = tm.split("-")
            year = int(tm_split[0])
            month = int(tm_split[1])
            day = int(tm_split[2])
            current_month = string_month_from_full_date(year, month, day)
            time.append(current_month)
        average_waterlevel = round( stat.mean(waterlevel) , 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )

    if x == 'all':
        name = 'All'
        label = "Time"
        cursor.execute(" SELECT time, water_level FROM ( SELECT * from iot_wqms_table ORDER BY id DESC ) order by id asc") 
        data = cursor.fetchall()
        del time[:]
        del waterlevel[:]
        for datum in data:
            datum_float = float(datum[1])   # ph data in float
            waterlevel.append(datum_float)        # pushing to ph list
            tm = str(datum[0][:7])
            time.append(tm)
        average_waterlevel = round( stat.mean(waterlevel) , 2)
        min_waterlevel = round(min(waterlevel), 2)
        max_waterlevel = round(max(waterlevel), 2)
        range_waterlevel = float( round((max_waterlevel - min_waterlevel), 2) )
    
    return render_template("waterlevelChart.html", waterlevel=waterlevel, time=time, label=label, name=name, average_waterlevel=average_waterlevel, min_waterlevel=min_waterlevel, max_waterlevel=max_waterlevel, range_waterlevel=range_waterlevel)



@app.route("/dashboard", methods=["GET"])
def dashboard():
    print(">>> dashboard running ...")
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    # selecting current hour data ...ie, 120 for every 30 seconds of posting
    cursor.execute(" SELECT * FROM iot_wqms_table ORDER BY id DESC LIMIT 120") 
    data = cursor.fetchall()
    data = list(data)

    print(".........Page refreshed at", datetime.datetime.now())

    # data collector
    temp_data = []
    turbidity_data = []
    ph_data = []
    waterlevel_data = []

    # collecting individual data to collectors
    for row in data:
        temp_data.append(row[2])   
        turbidity_data.append(row[3])
        ph_data.append(row[4])
        waterlevel_data.append(row[5])

    # last value added to database...current data recorded 
    last_temp_data = temp_data[0]
    last_turbidity_data = turbidity_data[0]
    last_ph_data = ph_data[0]
    last_waterlevel_data = waterlevel_data[0]


    # message toasting 
    if (last_temp_data < 23) | (last_temp_data > 34):
        flash("Abnormal Water Temperature", 'warning')
    if (last_turbidity_data < 0) | (last_turbidity_data > 5):
        flash("Abnormal Water Turbidity", 'warning')
    if (last_ph_data < 6) | (last_ph_data > 10):
        flash("Abnormal Water pH", 'warning')
    if (last_waterlevel_data < 5) | (last_waterlevel_data > 27):
        flash("Abnormal Water Level", 'warning')

    # current sum of 1hour data rounded to 2dp
    current_temp_sum = round(sum(temp_data), 2)
    current_turbidity_sum = round(sum(turbidity_data), 2)
    current_ph_sum = round( sum(ph_data), 2 )
    current_waterlevel_sum = round( sum(waterlevel_data), 2)  
    
    # fetching 240 data from db to extract the penultimate 120 data to calculate percentage change
    cursor.execute(" SELECT * FROM iot_wqms_table ORDER BY id DESC LIMIT 240") 
    data = list(cursor.fetchall())

    # collecting individual data
    prev_temp_data = []  # collecting temp values
    prev_turbidity_data = []
    prev_ph_data = []
    prev_waterlevel_data = []
    for row in data:
        prev_temp_data.append(row[2])
        prev_turbidity_data.append(row[3])
        prev_ph_data.append(row[4])
        prev_waterlevel_data.append(row[5])

    # slicing for immediate previous 120 data 
    prev_temp_data = prev_temp_data[120:240]
    prev_temp_sum = round( sum(prev_temp_data), 2 )

    prev_turbidity_data = prev_turbidity_data[120:240]
    prev_turbidity_sum = round( sum(prev_turbidity_data), 2 )

    prev_ph_data = prev_ph_data[120:240]
    prev_ph_sum = round( sum(prev_ph_data), 2 )

    prev_waterlevel_data = prev_waterlevel_data[120:240]
    prev_waterlevel_sum = round( sum(prev_waterlevel_data), 2 )

    # temp, getting the percentage change
    temp_change = prev_temp_sum - current_temp_sum
    temp_change = round(temp_change, 2)
    percentage_temp_change = (temp_change/current_temp_sum) * 100
    percentage_temp_change = round(percentage_temp_change, 1)
    
    # ph, getting the percentage change
    ph_change = prev_ph_sum - current_ph_sum
    ph_change = round(ph_change, 2)
    percentage_ph_change = (ph_change/current_ph_sum) * 100
    percentage_ph_change = round(percentage_ph_change,1)

    # turbidity, getting the percentage change
    turbidity_change = prev_turbidity_sum - current_turbidity_sum
    turbidity_change = round(turbidity_change, 2)
    percentage_turbidity_change = (turbidity_change/current_turbidity_sum) * 100
    percentage_turbidity_change = round(percentage_turbidity_change,1)

    # waterlevel, getting the percentage change
    waterlevel_change = prev_waterlevel_sum - current_waterlevel_sum
    waterlevel_change = round(waterlevel_change, 2)
    percentage_waterlevel_change = (waterlevel_change/current_waterlevel_sum) * 100
    percentage_waterlevel_change = round(percentage_waterlevel_change,1)


    # notification toast 
    # flash("Not So OK", 'error')

    return render_template("dashboard.html", data=data, percentage_temp_change=percentage_temp_change, percentage_ph_change=percentage_ph_change, percentage_turbidity_change=percentage_turbidity_change, percentage_waterlevel_change=percentage_waterlevel_change, temp_change=temp_change, ph_change=ph_change, turbidity_change=turbidity_change, waterlevel_change=waterlevel_change, last_temp_data=last_temp_data, last_ph_data=last_ph_data, last_turbidity_data=last_turbidity_data, last_waterlevel_data=last_waterlevel_data)



"""
This section prepares and download the data in csv format for analysis
Created: 31st May, 2019 by John PK Erbynn
Ack: Dennis Effa Amponsah

NB: prop implies property(of water)
"""

@app.route("/download/<prop>")
def get_CSV(prop):
    print(">>> csv file downloaded")

    if prop == 'temperature':
        # prepare data in csv format
        generator.generate_csv_file(prop)

        # opens, reads, closes csv file for download 
        with open(f'data/wqms_{prop}_data.csv', 'r') as csv_file:
            csv_reader = csv_file.read().encode('latin-1')
        csv_file.close()

        # routes function returning the file download
        return Response(
            csv_reader,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=wqms_%s.csv" %prop}
        )
    

    if prop == 'turbidity':
        generator.generate_csv_file(prop)
        with open(f'data/wqms_{prop}_data.csv', 'r') as csv_file:
            csv_reader = csv_file.read().encode('latin-1')
        csv_file.close()

        return Response(
            csv_reader,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=wqms_%s.csv" %prop}
        )


    if prop == 'ph':
        generator.generate_csv_file(prop)
        with open(f'data/wqms_{prop}_data.csv', 'r') as csv_file:
            csv_reader = csv_file.read().encode('latin-1')
        csv_file.close()

        return Response(
            csv_reader,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=wqms_%s.csv" %prop}
        )
    

    if prop == 'water_level':
        generator.generate_csv_file(prop)
        with open(f'data/wqms_{prop}_data.csv', 'r') as csv_file:
            csv_reader = csv_file.read().encode('latin-1')
        csv_file.close()

        return Response(
            csv_reader,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=wqms_%s.csv" %prop}
        )
       


# main function
if  __name__ == "__main__":
    try:
        # using local ip address and auto pick up changes
        app.run(debug=True)

        # create database for the system if on not created
        create_database.create_table()

        # using static ip
        # app.run(debug=True, host='192.168.43.110 ', port=5050)   # setting your own ip

    except Exception as rerun:
        print(">>> Failed to run main program : ",rerun)
