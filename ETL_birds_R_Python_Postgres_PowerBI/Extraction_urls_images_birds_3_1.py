# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:39:24 2022

@author: samee
"""

from Transformation_bird_data_3 import bird_data_transform
from Transformation_bird_data import bird_data_transform
from duckduckgo_search import ddg

from duckduckgo_search import ddg_images

import sys

# Path where the files (csv and other data) is stored on local machine should be provided

sys.path.append('G:/.....')

# The data from the Transformed_data python file, the dataset bird_data_transform is imported and used for obtaining the urls


# Obtain the list of scientific names from the transformed data

bird_names = bird_data_transform['scientific_name'].unique().tolist()

bird_names

# Function to obtain the urls of images


def obtain_url(x):
    y = ddg_images(x, region='wt-wt', safesearch='Off', size=None, color='color',
                   type_image=None, layout=None, license_image=None, max_results=1)

    res = y[0]['image']

    res_list = [res, x]

    return(res_list)

# Obtaining the urls


results = list(map(obtain_url, bird_names))

# Creating a pandas DataFrame from the list

url_data = pd.DataFrame(results, columns=['url', 'scientific_name'])

# Exporting the dataframe as a csv (optional)

# url_data.to_csv('url_data.csv')
