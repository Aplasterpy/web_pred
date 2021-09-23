#Import Library
from flask import Flask, render_template, request, redirect, url_for, Response
import os
import urllib.request
import pyodbc

app = Flask(__name__)

#Database Connection using pyodbc
#server = 'WIN-OE3JAUO9CMD' 
#database = 'MaxAIML' 
#username = 'MaxAIML' 
#password = 'MaxAIML@#321'
#tcon = 'yes'  

connection = pyodbc.connect(Driver='{SQL Server}', Server= "WIN-OE3JAUO9CMD", Database="MaxAIML", User ="MaxAIML", pwd="MaxAIML@#321")
cursor = connection.cursor()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result")
def result():
    return render_template("report.html")



@app.route("/data", methods = ['GET', 'POST'])
def data():
    cursor.execute("select * from CokeCalender")
    data = cursor.fetchall()
    return render_template("index.html", data=data)


    



if __name__ == '__main__':
    app.run(debug = True)