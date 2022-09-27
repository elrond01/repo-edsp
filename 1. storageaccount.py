# Databricks notebook source




configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": ,
       "fs.azure.account.oauth2.client.secret": "kvsecret",
       "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/16b3c013-d300-468d-ac64-7eda0820b6d3/oauth2/token",
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

dbutils.fs.mount(
source = "abfss://container@sademocol.dfs.core.windows.net",
mount_point = "/mnt/demodata",
extra_configs = configs)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

spark.conf.set("fs.azure.account.key.sademocol.dfs.core.windows.net","AnL7gO+xB5rDZG0O5eg8dsgSnKouO0bdDN2JtM3eFnvau4WJ01TcBA82BtzYvNrQTlWVlVheNOxc+AStdWUCqQ==")
df=spark.read.csv(path='abfss://container@sademocol.dfs.core.windows.net/role-assignments-2022-07-21.csv',header= True)
display(df)


# COMMAND ----------

spark.conf.set("fs.azure.account.key.sademocol.dfs.core.windows.net",dbutils.secrets.get("demoscope","kvsecret"))

# COMMAND ----------

# Python code to mount and access Azure Data Lake Storage Gen2 Account to Azure Databricks with Service Principal and OAuth
# Author: Dhyanendra Singh Rathore

# Define the variables used for creating connection strings
adlsAccountName = "sademocol"
adlsContainerName = "container"
mountPoint = "/mnt/data"

# Application (Client) ID
applicationId = dbutils.secrets.get(scope="demoscope",key="kvappid")

# Application (Client) Secret Key
authenticationKey = dbutils.secrets.get(scope="demoscope",key="kvappsecret")

# Directory (Tenant) ID
tenandId = dbutils.secrets.get(scope="demoscope",key="kvtenantid")

endpoint = "https://login.microsoftonline.com/" + tenandId + "/oauth2/token"
source = "abfss://" + adlsContainerName + "@" + adlsAccountName + ".dfs.core.windows.net" 

# Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": authenticationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

# Mounting ADLS Storage to DBFS
# Mount only if the directory is not already mounted
if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
  dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------


