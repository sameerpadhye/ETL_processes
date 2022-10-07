# Appending the daily observational data to the data table

# In order to obtain the data everyday, the steps involved are almost the same as used in creating the database and table. This file is then added to the Windows task scheduler with execution of this file scheduled daily for a specified period at a specific time

# Importing the libraries

from ebird.api import get_observations

import pandas as pd

from sqlalchemy import create_engine,text

from sqlalchemy_utils import database_exists,create_database

# API key (should be added in between the quotes)

api_key='.....'

# Getting observations from the database for the specified region everyday

obs=get_observations(api_key, "IN-MH-PU",back=1)

# Getting observations from the database for the specified region using the API key. Here, the argument 'back' = 1 will obtain the data immediately after the first day's data has been collected (after executing the database creation file)

data = pd.json_normalize(obs)

# Connect to the database and append the new data to the database (credentials need to be added). Use the same names of database and table assigned while creating the database and table (i.e. ebirds and birds_data_daily will change as per the user)

# Establishing the connection

engine = create_engine("postgresql://postgres:......./ebirds")
if not database_exists(engine.url):
    create_database(engine.url)
    
# Appending the data to the table    

data.to_sql('birds_data_daily', con=engine, index=True,
                index_label='id', if_exists='append')

engine.dispose()
