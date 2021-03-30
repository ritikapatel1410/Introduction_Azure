"""
@Author: Ritika Patidar
@Date: 2021-03-29 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-29 10:10:38  
@Title : perform basic operation on azure cosmodb
"""

import os
import sys
from azure.cosmos import CosmosClient
from azure.cosmos.partition_key import PartitionKey
from pydocumentdb import document_client
from decouple import config
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile


class cosmo_db:
    def __init__(self):
        endpoint=config('cdb_endpoint') 
        key=config('cdb_key')
        self.client = CosmosClient(endpoint, key)
        self.database_name = config('cdb_database_name')
        self.container_name = 'FamilyContainer'
    def create_database(self):
        try:
            database = self.client.create_database_if_not_exists(id=self.database_name)
            loggerfile.Logger("info","successfully create database")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def create_cointainer(self):
        try:
            container = database.create_container_if_not_exists(id=self.container_name,partition_key=PartitionKey(path="/lastname"),offer_throughput=400)
            container = database.get_container_client(self.container_name)
            loggerfile.Logger("info","successfully create container")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def insert_data(self):
        try:
            name_detail=[("ritika","patidar"),("dipali","patel"),("vijay","patidar")]
            for index,value in enumerate(name_detail):
                container.upsert_item({
                    'id': 'item{0}'.format(index),
                    'firstname': value[0],
                    'lastname': value[1]
                    }
                    )
            loggerfile.Logger("info","successfully insert data")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def read_data(self):
        try:
            query = 'SELECT * FROM c'
            item_list = list(container.read_all_items(max_item_count=10))
            for doc in item_list:
                    print('Item Id: {0:10}firstname: {1:10}lastname: {2}'.format(doc.get('id'),doc.get('firstname'),doc.get('lastname')))
            loggerfile.Logger("info","successfully read data")
        except expection as error:
            loggerfile.Logger("error","{0} error occured".format(error))