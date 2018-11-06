import sqlite3
import random
import time
# import matplotlib.pyplot

# conect = sqlite3.connect('pk.db')
conect = sqlite3.connect('pk.db', check_same_thread=False)
cursor = conect.cursor()

def create_table():
    cursor.execute( 
        """ CREATE TABLE IF NOT EXISTS pk( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    temp REAL, 
                    humidity REAL, 
                    ph REAL, 
                    salinity REAL) """)


# def data_entry():
#     cursor.execute(
#         """ INSERT INTO pk(temp, humidity, ph, salinity) 
#             VALUES(23,56,35.3,40.3) """)
#     conect.commit()


def dynamic_data_entry():
    temp = random.randrange(10, 50)
    humidity = random.randrange(10, 30)
    ph = random.randint(0, 10)
    salinity = random.randint(50, 120)
    cursor.execute(""" INSERT INTO pk(temp, humidity, ph, salinity) VALUES (?, ?, ?, ?) """,
                    (temp, humidity, ph, salinity))
    conect.commit()     #commit function only associated with the connection
    


def read_data_from_db():
    cursor.execute(" SELECT temp, humidity FROM pk ")
    copy_data = cursor.fetchall()
    # for row in copy_data:
    #     print(row)
    data_list = list(copy_data)
    return data_list
    

# create_table()

# for i in range(5):    
#     dynamic_data_entry()
#     time.sleep(1)
for row in read_data_from_db():
    print(row)
# print(read_data_from_db())
 
# data_entry()

# cursor.close()
# conect.close()  #stops the database and prevent memory usage


######################################################### End of Data_base #####################################







# insert = """
#              INSERT INTO pk(temp, humidity, ph, salinity) 
#              VALUES(100,200,300,400)
#          """
# cursor.execute(insert)


# data_entry()


# def get_values():
#     cursor.execute("SELECT * FROM pk")
#     return list(cursor.fetchall())

# get_values()

# print(create_table())
# print(data_entry())
# print(get_values())







# query = """
#         CREATE TABLE IF NOT EXISTS pk( 
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
#             INSERT INTO pk(temp, humidity, ph, salinity) 
#             VALUES(24,50,45.3,40.3)
#         """

# sal = 40
# p=25
# hum=44
# temp=35
# insert3 = """INSERT INTO pk(temp, humidity, ph, salinity) 
#              VALUES(?, ?, ?, ?)"""



# cursor.execute(insert)
# cursor.execute(insert3, (temp,hum, p, sal))



# def get_values():
#     select = """
#             SELECT * FROM pk
#         """
#     cursor.execute(select)

#     return list(cursor.fetchall())

# print(get_values())



# print(copy_data)