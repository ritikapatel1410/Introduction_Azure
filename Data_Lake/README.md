# Azure Data Lake

* perform basic data upload on Azure Data Lake

* Create a Data Lake Storage Gen1 account
  * step 1 : Sign on to the new Azure portal and Click Create a resource > Storage > Data Lake Storage Gen1.
  * step 2 : enter all given fileds and in Encryption Setting select Use keys from your own Key Vault then Click OK in the Encryption Settings 
  * step 3 : Click on Create.
* Assign permissions to Azure Key Vault.
  * step 1 : If you used keys from the Azure Key Vault, the blade for the Data Lake Storage Gen1 account displays a warning at the top. Click the warning to open Encryption.
  * step 2 : The blade shows two options to configure access.
  * step 3 : In the first option, click Grant Permissions to configure access. The first option is enabled only when the user that created the Data Lake Storage Gen1 account is also an admin for the Azure Key Vault.
  * The other option is to run the PowerShell cmdlet displayed on the blade. You need to be the owner of the Azure Key Vault or have the ability to grant permissions on the Azure Key Vault. After you have run the cmdlet, come back to the blade and click Enable to configure access.

* Reference :
  * https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-portal
  * https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-overview
  

