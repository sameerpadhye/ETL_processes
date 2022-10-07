## Scheduling the extraction and integration of observational data into the bird database

Extraction and integration: Python & postgreSQL
Scheduling: Windows Task scheduler
Transformation: postgreSQL
Loading: Python & postgreSQL

The aim of this project was to automate the data extraction of observational data from a specific region for a period of 1 month
followed by transformation and loading in a postgreSQL database.Although, postgreSQL has been used initially for both Extraction and loading data , Azure postgreSQL will be used
as a data warehouse in the near future

#1. Extraction 

Species data was extracted using the ebird api in Python. Since the data was in a JSON format, it was converted in a tabular form (pandas dataframe) and stored in a postgreSQL database

#2. Scheduling the task

Task scheduler in Windows was used to schedule a daily download of the data for a period of 1 month. The Python script used to extract the data was used here followed by appending it to the data table

#3  Transformation and Loading 

The bird data was transformed (and loaded) in a postgreSQL database


The project is still being edited and updated.

* The API key and Database connection details have been removed from the script. File paths subject to change


 