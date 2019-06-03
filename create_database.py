"""
This module creates sqlite database 

"""


import sqlite3
import random
import datetime
import time

con = sqlite3.connect('iot_wqms_data.db')
# con = sqlite3.connect(':memory:') # when db locks
cursor = con.cursor()

def create_table():

        cursor.execute( 
                """ CREATE TABLE IF NOT EXISTS iot_wqms_table( 
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        temperature REAL, 
                        turbidity REAL, 
                        ph REAL, 
                        water_level REAL) """)
                        
        print('...inside create db fxn') 

# if not included, creates only DB without any table    
create_table()



# def dynamic_data_entry():
#     con = sqlite3.connect('aquaBase.db')
#     cursor = con.cursor()

#     temp = random.randrange(10,20)
#     humidity = random.randrange(10, 30)
#     ph = random.randint(0, 10)
#     salinity = random.randint(50, 120)
#     cursor.execute(""" INSERT INTO aquaBaseTable(temp, humidity, ph, salinity) VALUES (?, ?, ?, ?) """,
#                     (temp, humidity, ph, salinity))
#     con.commit()     #commit function only associated with the connection
    


# def read_data_from_db():
#     con = sqlite3.connect('aquaBase.db')
#     cursor = con.cursor()

#     cursor.execute(" SELECT * FROM aquaBaseTable ")
#     copy_data = cursor.fetchall()
#     # for row in copy_data:
#     #     print(row)
#     # data_lis__name__, representing the current file t = list(copy_data)
#     return copy_data
    

# create_table()
# for i in range(5):    
#     dynamic_data_entry()
#     time.sleep(1)

# for row in read_data_from_db():
#     print(row):memory::memory::memory:memory::memory::memory::memory::
# read_data_from_db()
 
# data_entry()

# cursor.close()
# con.close()  #stops the database and prevent memory usage


######################################################### End of Data_base #####################################







# insert = """
#              INSERT INTO aquaBase(temp, humidity, ph, salinity) 
#              VALUES(100,200,300,400)
#          """
# cursor.execute(insert)


# data_entry()


# def get_values():
#     cursor.execute("SELECT * FROM aquaBase")
#     return list(cursor.fetchall())

# get_values()

# print(create_table())aquaBaseTable
# print(data_entry())
# print(get_values())







# query = """
#         CREATE TABLE IF NOT EXISTS aquaBase( 
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
#             INSERT INTO aquaBase(temp, humidity, ph, salinity) 
#             VALUES(24,50,45.3,40.3)
#         """

# sal = 40
# p=25
# hum=44
# temp=35
# insert3 = """INSERT INTO aquaBase(temp, humidity, ph, salinity) 
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