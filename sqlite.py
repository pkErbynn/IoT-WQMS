import sqlite3
conect = sqlite3.connect('aquatech.db')
cursor = conect.cursor()

# def create_table():
#     cursor.execute( 
#         """ CREATE TABLE IF NOT EXISTS aquatech( 
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                     Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
#                     temp REAL, 
#                     humidity REAL, 
#                     ph REAL, 
#                     salinity REAL) """)
# create_table()

# def data_entry():
#     cursor.execute(
#         """ INSERT INTO aquatech(temp, humidity, ph, salinity) 
#             VALUES(23,56,35.3,40.3) """)
    # conect.commit()
    # cursor.close()
#    #conect.close()
# insert = """
#              INSERT INTO aquatech(temp, humidity, ph, salinity) 
#              VALUES(100,200,300,400)
#          """
# cursor.execute(insert)


# # data_entry()


# def get_values():
#     cursor.execute("SELECT * FROM aquatech")
#     return list(cursor.fetchall())

# get_values()

# print(create_table())
# print(data_entry())
# print(get_values())







query = """
        CREATE TABLE IF NOT EXISTS aquatech( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Time TIMESdTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    temp REAL, 
                    humidity REAL, 
                    ph REAL, 
                    salinity REAL
                )
        """
cursor.execute(query)
conect.commit()
# conect.close() cannot operate on a closed database
# cursor.close() cannot operate on a closed cursor


insert = """
            INSERT INTO aquatech(temp, humidity, ph, salinity) 
            VALUES(24,50,45.3,40.3)
        """

sal = 40
p=25
hum=44
temp=35
insert3 = """INSERT INTO aquatech(temp, humidity, ph, salinity) 
             VALUES(?, ?, ?, ?)"""



cursor.execute(insert)
cursor.execute(insert3, (temp,hum, p, sal))



def get_values():
    select = """
            SELECT * FROM aquatech
        """
    cursor.execute(select)

    return list(cursor.fetchall())

print(get_values())


# conect.close()
# cursor.close(/)


