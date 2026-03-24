from flask import *
import os
from flask_cors import CORS

# CORS = cross origin resourse sharing

#Import pymysql library that will enable you to create a connection btwn vscode and the db(sql)
import pymysql

#Create a webapp
app = Flask (__name__)
CORS(app)

#Configure the location to whwre your product image will be saved on your application 
app.config["UPLOAD_FOLDER"] = "static/images"

#Below is the signup route (registration )
@app.route("/api/signup", methods = ["POST"])
def signup():
    if request.method == "POST":
        #Extract the different details entered on the form 
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        phone = request.form["phone"]

        #Create/establish a connection to the database
        connection = pymysql.connect(host="mysql-preciouswanjiku.alwaysdata.net", user = "preciouswamjiku", password= "modcom1234", database= "preciouswanjiku_sokogarden")

        #Create a cursor
        cursor = connection.cursor()
        #Structure the sql query to insert data into the table
        sql = "INSERT INTO users (username, password, email, phone) VALUES(%s, %s, %s, %s)"
        #Put the data into a tuple
        data = (username, password, email, phone)
        #Use the cursor to execute the sql as you replace the placeholder with the actual data
        cursor.execute(sql, data)
