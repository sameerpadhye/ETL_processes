# -*- coding: utf-8 -*-
"""
Loading the transformed bird data into postgreSQL

"""
from Extraction_urls_images_birds_3_1 import url_data

from Transformation_bird_data_3 import bird_data_transform

import pandas as pd

from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists, create_database

# The directory path of the sourced file and this file was not present in the Python paths and hence added

import sys

sys.path.append(
    'G:\Research data\Other groups\Ebird_data\ETL_birds_R_Python_Postgres_PowerBI')

# The data from the Transformed_data is imported


# Establishing connection to the postgreSQL database using sqlalchemy and creating a database to host the table

engine = create_engine("postgresql://postgres:gambitsam19*%@localhost/ebirds")
if not database_exists(engine.url):
    create_database(engine.url)

# Writing the birds and url data to the database

bird_data_transform.to_sql('birds_data', con=engine, if_exists='replace')

url_data.to_sql('url_data', con=engine, if_exists='replace')

# Closing the connection

engine.dispose()
