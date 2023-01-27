import random

import mysql.connector as mys
from datetime import datetime



myconnect=mys.connect(host='localhost',user='root',passwd='9977',database='Hotel',auth_plugin='mysql_native_password')
print(myconnect)
cursor=myconnect.cursor()

room_type=['SEA_FACING','POOL_VIEW','GARDEN_VIEW','SUITE']

def Check_in(name,room_type):

    cursor.execute(f"SELECT RoomNo FROM CUSTOMER WHERE Roomtype='{room_type}' and Date_Check_in IS NULL")
    roomsfree=cursor.fetchall()
    room_number=int(random.choice(roomsfree)[0])
    check_in_date=datetime.now()
    cursor.execute(f"UPDATE CUSTOMER SET DATE_CHECK_IN = '{check_in_date}',Name='{name}' WHERE RoomNO= {room_number}")
    myconnect.commit()
    return room_number


def Check_out(room_number):

    if 0< room_number <=300:

        cursor.execute(f"SELECT Name,DATE_CHECK_IN,ROOMTYPE FROM CUSTOMER WHERE ROOMNO= {room_number}")
        data = cursor.fetchall()
        name_original = data[0][0]

        cursor.execute(f"UPDATE CUSTOMER SET DATE_CHECK_IN = NULL,NAME='NULL' WHERE ROOMNO={room_number}")

        Date_check_out = datetime.now()
        Date_check_in = data[0][1]
        room_type = data[0][2]
        cursor.execute(f"INSERT INTO PREV_CUST VALUES('{name_original}',{room_number},'{room_type}','{Date_check_in}','{Date_check_out}')")
        myconnect.commit()





    else:
        return "Invalid Room Number!!"


def display_details(roomno):

    cursor.execute(f"SELECT * FROM CUSTOMER WHERE RoomNo ='{roomno}' ")
    search=cursor.fetchall()


    return (search[0][1:])





























