"""
@Author: Ritika Patidar
@Date: 2021-03-23 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-23 10:10:38  
@Title : perform basic operation on azure sql database 
"""
import sys
import os
import pyodbc 
from decouple import config
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile

class sql_database:
    def init(self):
        server = config('SQL_server') 
        database = config('SQL_database')  
        username = config('SQL_username') 
        password = config('SQL_password ')
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.cnxn.cursor()
    def create_table(self):
        try:
            self.cursor.execute(''' CREATE TABLE IF NOT EXISTS People (Name nvarchar(50),Age int,City nvarchar(50)) ''')
            self.cnxn.commit()
            loggerfile.Logger("info","successfully create table")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def insert_data(self):
        try:
            self.cursor.execute(''' INSERT INTO People (Name, Age, City) VALUES('ritika',23,'indore')''')
            self.cnxn.commit()
            loggerfile.Logger("info","successfully insert data")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def read_data(self):
        try:
            mycursor=cursor.execute(''' SELECT * FROM People ''')
            result=mycursor.fetchall()
            for data in result:
                print(data)
            loggerfile.Logger("info","successfully read data")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))