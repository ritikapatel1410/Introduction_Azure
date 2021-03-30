'''
 @Author: Ritika Patidar
 @Date: 2021-03-29 12:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-03-29 12:15:38  
 @Title : perform operation on data lake Azure 
'''
from azure.common.credentials import ServicePrincipalCredentials
from azure.common.credentials import UserPassCredentials
from msrestazure.azure_active_directory import AADTokenCredentials
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount
from azure.datalake.store import core, lib, multithread
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup
import logging, getpass, pprint, uuid, time
import os
import sys
from decouple import config
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile

def main():
    """
        Description:
            this function is define for data lake basic operation
        Parameter:
            None
        Return:
            None
    """
    try:
        subscriptionId = config('dl_subscriptionId') 
        adlsAccountName = config('dl_adlsAccountName') 
        adlCreds = lib.auth(tenant_id = config('dl_tenant_id'), client_secret = config('dl_client_secret'), client_id = config('dl_client_id'), resource = 'https://datalake.azure.net/')
        adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=adlsAccountName)
        adlsFileSystemClient.mkdir('/mysampledirectory')
        multithread.ADLUploader(adlsFileSystemClient, lpath='data/mysamplefile.txt', rpath='/mysampledirectory/mysamplefile.txt', nthreads=64, overwrite=True, buffersize=4194304, blocksize=4194304)
        loggerfile.Logger("info","successfully upload data into datalake")
    except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
main()