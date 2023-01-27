import mysql.connector as mysql
import datetime
#
def sign_up(name, email, password):
    db = mysql.connect(host='localhost',user='root',passwd='9977',database='Hotel',auth_plugin='mysql_native_password')
    mycursor = db.cursor()
    t = datetime.datetime.now()
    mycursor.execute(f"INSERT INTO USER (name, email, password) Values (\'{name}\',\'{email}\',\'{password}\')")
    db.commit()

def log_in(email):
    db = mysql.connect(host='localhost',user='root',passwd='9977',database='Hotel',auth_plugin='mysql_native_password')
    mycursor = db.cursor()
    mycursor.execute(f"SELECT PASSWORD FROM USER WHERE EMAIL = \'{email}\'")
    p = ""
    for x in mycursor:
        p = x[0]
    password = p
    return password
