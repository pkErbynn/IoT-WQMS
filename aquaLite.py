import sqlite3
import random
import datetime
import time


def create_table():
    # con = sqlite3.connect('iot_wqms_data.db')
    con = sqlite3.connect(':memory:')
    cursor = con.cursor()

    cursor.execute( 
        """ CREATE TABLE IF NOT EXISTS iot_wqms_table( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    temperature REAL, 
                    turbidity REAL, 
                    ph REAL, 
                    water_level REAL) """
    )

    con.commit()   # without commit, error


def post_dynamic_data_entry():
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    temperature = random.randrange(10,20)
    turbidity = random.randrange(10, 30)
    ph = random.randint(0, 10)
    water_level = random.randint(50, 120)
    cursor.execute(""" INSERT INTO iot_wqms_table(temperature, turbidity, ph, water_level) 
                       VALUES (?, ?, ?, ?) """,
                    (temperature, turbidity, ph, water_level))
    con.commit()     #commit function only associated with the connection
    


def read_all_data_from_db():
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    cursor.execute(" SELECT * FROM iot_wqms_table ")
    fetch_data = cursor.fetchall()
    # for row in fetch_data:
    #     print(row)
    # data_lis__name__, representing the current file t = list(fetch_data)
    return fetch_data
    

def read5_data_from_db():
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    cursor.execute(" SELECT * from (select * FROM iot_wqms_table ORDER BY id DESC LIMIT 5) ORDER by id ASC")
    fetch_data = cursor.fetchall()

    # for row in fetch_data:
    #     print(row)
    # data_lis__name__, representing the current file t = list(fetch_data)
    return fetch_data

# create_table()
# for i in range(5):    
#     dynamic_data_entry()
# #     time.sleep(1)

# for row in read_data_from_db():
#     print(row):memory::memory::memory:memory::memory::memory::memory::

# post_dynamic_data_entry()
# print(read5_data_from_db())
 
# data_entry()

# cursor.close()
# con.close()  #stops the database and prevent memory usage


######################################################### End of Data_base #####################################




############################# ANOTHER LEVEL ################################################################################

def push_Data(data):
    con = sqlite3.connect('iot_wqms_data.db')
    cursor = con.cursor()

    # print("temperature:", data['temperature'])

    cursor.execute(""" INSERT INTO iot_wqms_table( temperature, turbidity, ph, water_level) 
                       VALUES (?, ?, ?, ?) """,
                   (data["temperature"], data["turbidity"], data["ph"], data["water_level"]))
    con.commit()








#############################################################################################################
# insert = """
#              INSERT INTO iot_wqms_data(temp, humidity, ph, salinity) 
#              VALUES(100,200,300,400)
#          """
# cursor.execute(insert)


# data_entry()


# def get_values():
#     cursor.execute("SELECT * FROM iot_wqms_data")
#     return list(cursor.fetchall())

# get_values()

# print(create_table())
# print(data_entry())
# print(get_values())







# query = """
#         CREATE TABLE IF NOT EXISTS iot_wqms_data( 
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                     Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
#                     temp REAL, 
#                     humidity REAL, 
#                     ph REAL, 
#                     salinity REAL
#                 )
#         """
# cursor.execute(query)



# insert = """
#             INSERT INTO iot_wqms_data(temp, humidity, ph, salinity) 
#             VALUES(24,50,45.3,40.3)
#         """

# sal = 40
# p=25
# hum=44
# temp=35
# insert3 = """INSERT INTO iot_wqms_data(temp, humidity, ph, salinity) 
#              VALUES(?, ?, ?, ?)"""



# cursor.execute(insert)
# cursor.execute(insert3, (temp,hum, p, sal))



# def get_values():
#     select = """
#             SELECT * FROM aqua_a
#         """
#     cursor.execute(select)

#     return list(cursor.fetchall())

# print(get_values())