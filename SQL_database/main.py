"""
@Author: Ritika Patidar
@Date: 2021-03-28 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-28 10:10:38  
@Title : main code perform basic operation on Azure ASQL database
"""

from sql_operation import sql_database
import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile

def main():
    try:
        sql_database_OBJ=sql_database()
        mode=int(input("===================================================select mode of azure sql database====================================================\n0 : create table\n====================================\n1 : insert data\n==============================================\n2 : show sata\n==================================================================\n3 : quit\n===============================================================\nenter: "))
        if(mode==0):
            Basic_CRUD_DB_OBJ.create_table()
        elif(mode==1):
            Basic_CRUD_DB_OBJ.insert_data()
        elif(mode==2):
            Basic_CRUD_DB_OBJ.read_data(self)
        elif(mode==3):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
        #break
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))


main()