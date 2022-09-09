# -*- coding: utf-8 -*-
"""
Data transformation of bird dataset

@author: sameer padhye
"""
# Packages for Data trasnformation

import pandas as pd

from datetime import datetime as dt

import numpy as np

# Import data (Path where the csv file is stored)

bird_data = pd.read_csv("G:/....")

# Column names of the data

bird_data.columns

# Information on the data types

bird_data.info()

# Checking the number of rows and columns

bird_data.shape

# Renaming some of the columns

bird_data.rename(columns={"sciName": "scientific_name", "locName": "locality", "lat": "latitude", "lng": "longitude","obsDt": "obs_date", "comName": "common_name", 'obsValid': 'valid', 'obsReviewed': 'reviewed', 'howMany': 'count'}, inplace=True)

# Rechecking the column names

bird_data.columns

# Converting the date column to date data type

bird_data['obs_date'] = pd.to_datetime(bird_data['obs_date'])

# Rechecking the data types

bird_data.info()

# Checking null values in the dataset

bird_data.isna().sum()

# There are many rows of counts column where data are not available

# Selecting the relevant columns for analysis

bird_data_transform = bird_data.loc[:, ['common_name', 'scientific_name',                                        'locality', 'latitude', 'longitude', 'obs_date', 'count', 'reviewed']]

# Checking the number of rows and columns of the edited dataset

bird_data_transform.shape

# Creating list of common names

column_names = bird_data_transform.select_dtypes(object).columns

print(column_names)

# Checking and removing duplicates

bird_data_transform[bird_data_transform.duplicated()]

bird_data_transform.drop_duplicates(keep=False, inplace=True)

bird_data_transform.shape

# Checking for unidentified species in the data (given by sp. in the dataset)

len(bird_data_transform[bird_data_transform.scientific_name.str.contains(
    pat='sp.$')])

# There are no such instances

# Creating a separate month column using the dates for data summarization

bird_data_transform['Month'] = bird_data_transform['obs_date'].dt.month

bird_data_transform['Month'] = bird_data_transform['Month'].astype('category')

bird_data_transform.info()

# Removing text with parentheses with redundant GIS data present in the localities column

bird_data_transform.locality.str.match('\((.+)\)').sum()

bird_data_transform['locality'] = bird_data_transform.locality.str.replace(
    '\((.+)\)', '')

bird_data_transform.locality.str.match('\((.+)\)').sum()

# Removing any digits present in the localities column

bird_data_transform.locality.str.match('\d+').sum()

bird_data_transform['locality'] = bird_data_transform.locality.str.replace(
    '\d+', '')

bird_data_transform.locality.str.match('\d+').sum()

# Removing unspecified locality names present in the localities column

bird_data_transform.locality.str.match('^<u+.+').sum()

bird_data_transform['locality'] = bird_data_transform.locality.str.replace(
    '^<u.+', '')

bird_data_transform.locality.str.match('^<u+.+').sum()

# Remove '\n', '\' and other special characters from locality names

bird_data_transform['locality'] = bird_data_transform.locality.str.replace(
    '\n', '')

bird_data_transform['locality'] = bird_data_transform.locality.str.replace(
    '\\', '')

bird_data_transform['locality'] = bird_data_transform['locality'].str.replace(
    '[/._-]+', '')

# Select the initial section of the locality

bird_data_transform['locality'] = bird_data_transform.locality.str.split(
    ',', n=1).str.get(0)

# Remove the pune, maharashtra and in words from the locality column (This is done since the data are limited to Pune only)

bird_data_transform['locality'] = bird_data_transform['locality'].replace(
    '.+, pune, maharashtra, in', '')

# Remove addtional spaces in between the locality names

bird_data_transform.locality.replace(r'\s+', ' ', regex=True).head(50)

bird_data_transform['locality'] = bird_data_transform.locality.replace(
    r'\s+', ' ', regex=True)

bird_data_transform.locality.head(50)

# bird_data_transform.locality.head(50)

bird_data_transform[bird_data_transform['locality'] == '']

bird_data_transform['locality'] = bird_data_transform.locality.replace(
    r'', np.NaN, regex=True)

bird_data_transform['locality'] = bird_data_transform['locality'].fillna(
    'Location name not known')

# Trimming the blank spaces (if/any) in the text columns

bird_data_transform[column_names] = bird_data_transform[column_names].apply(
    lambda x: x.str.strip())

# Converting the text columns in appropriate case

bird_data_transform[column_names] = bird_data_transform[column_names].apply(
    lambda x: x.str.capitalize())
