# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "57f23281-c496-bc07-4e90-8640cef916d5",
# META       "default_lakehouse_name": "TestLHDemo",
# META       "default_lakehouse_workspace_id": "00000000-0000-0000-0000-000000000000",
# META       "known_lakehouses": [
# META         {
# META           "id": "57f23281-c496-bc07-4e90-8640cef916d5",
# META           "workspace_id": "00000000-0000-0000-0000-000000000000"
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
