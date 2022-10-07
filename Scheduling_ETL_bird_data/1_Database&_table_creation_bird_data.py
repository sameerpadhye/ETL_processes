# 1.Bird Database creation


# Importing necessary libraries 

from ebird.api import get_observations

import pandas as pd

from sqlalchemy import create_engine,text

from sqlalchemy_utils import database_exists,create_database

# API key (should be added in between the quotes)

api_key='.....'

# Getting observations from the database for the specified region using the API key. The location code signifies Pune, India. This can be edited as per user preference.

obs=get_observations(api_key, "IN-MH-PU")

# The output is obtained as a json. This is converted into a dataframe

data = pd.json_normalize(obs)

# This dataframe is then added to the postgres database (credentials need to be added while connecting to the database). Names of the database and tables can be changed as per convenience

# Connecting to the database

engine = create_engine("postgresql://postgres:......./ebirds")
if not database_exists(engine.url):
    create_database(engine.url)
    
data.to_sql('birds_data_daily', con=engine, index=True,
                index_label='id', if_exists='replace')

engine.dispose()
    
