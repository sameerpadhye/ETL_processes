# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:39:24 2022

@author: samee
"""

from duckduckgo_search import ddg

from duckduckgo_search import ddg_images

import sys

sys.path.append('G:/Research data/Other groups/Ebird_data/ETL_birds_R_Python_Postgres_PowerBI')

# The data from the Transformed_data is imported 

from Transformation_bird_data import bird_data_transform

# Obtain the list of scientific names from the transformed data

bird_names=bird_data_transform['scientific_name'].unique().tolist()

bird_names

# Function to obtain the urls of images 

def obtain_url(x):
    y = ddg_images(x, region='wt-wt', safesearch='Off',size=None,color='color',type_image=None, layout=None,license_image=None, max_results=1)
    
    res = y[0]['image']
    
    res_list = [res, x]
    
    return(res_list)

# Obtaining the urls
    
results = list(map(obtain_url,bird_names))

# Creating a pandas DataFrame from the list

url_data = pd.DataFrame(results, columns = ['url', 'scientific_name'])

# Exporting the dataframe as a csv (optional)

#url_data.to_csv('url_data.csv')

