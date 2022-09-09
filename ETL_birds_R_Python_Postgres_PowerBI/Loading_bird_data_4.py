# -*- coding: utf-8 -*-
"""
Loading the transformed bird data into postgreSQL

"""

import pandas as pd

from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists, create_database

# The directory path of the sourced data is called 

import sys

sys.path.append('G:\.......')

# The data from the bird_data and url_data is then imported

from Transformation_bird_data_3 import bird_data_transform

from Extraction_urls_images_birds_3_1 import url_data

# Establishing connection to the postgreSQL database using sqlalchemy and creating a database to host the table (details of hostname and password should be added)

engine = create_engine("postgresql://......../ebirds")
if not database_exists(engine.url):
    create_database(engine.url)

# Writing the birds and url data to the database

bird_data_transform.to_sql('birds_data', con=engine, if_exists='replace')

url_data.to_sql('url_data', con=engine, if_exists='replace')

# Closing the connection

engine.dispose()
