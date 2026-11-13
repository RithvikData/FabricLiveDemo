# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "cef916d5-8640-4e90-bc07-c49657f23281",
# META       "default_lakehouse_name": "TestLHDemo",
# META       "default_lakehouse_workspace_id": "4c6c5d41-f423-49e2-8a5a-21ed289e0665",
# META       "known_lakehouses": [
# META         {
# META           "id": "cef916d5-8640-4e90-bc07-c49657f23281"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.csv(path='abfss://Fabric_Dev_GitHub@onelake.dfs.fabric.microsoft.com/TestLHDemo.Lakehouse/Files/Development/EmpData.csv',header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format('delta').mode('append').saveAsTable('SalesEmpData')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
