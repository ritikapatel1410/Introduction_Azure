"""
@Author: Ritika Patidar
@Date: 2021-03-29 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-29 10:10:38  
@Title : main code perform basic operation on cosmodb
"""

from cosmodb_operation import cosmo_db
import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile

def main():
    try:
        cosmo_db_OBJ=cosmo_db()
        mode=int(input("===================================================select mode of cosmoDB====================================================\n0 : create database\n====================================\n1 : create cointainer\n==============================================\n2 : insert data\n==================================================================\n3 : read data\n===============================================================\n4 : quit\n=====================================================================\nenter : "))
        if(mode==0):
            cosmo_db_OBJ.create_database()
        elif(mode==1):
            cosmo_db_OBJ.create_cointainer()
        elif(mode==2):
            cosmo_db_OBJ.insert_data()
        elif(mode==3):
            cosmo_db_OBJ.read_data()
        elif(mode==4):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
        #break
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))


main()