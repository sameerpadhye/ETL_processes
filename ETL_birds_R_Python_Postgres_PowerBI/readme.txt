## A simple extraction, transformation, loading and visualization of a bird dataset of Pune, India

Extraction: R
Transformation: Python
Loading: Python & postgreSQL
Data Profiling and basic EDA: postgreSQL
Visualization: Microsoft Power BI 

# Extraction (files 1,2 & 3_1)

Species data was extracted using the ebird api from the 'ebird' package. R was specifically used as more data (6 months) could be easily acquired in a single operation using the ebird package. The data extracted
was saved as a csv 

The 'url' data was obtained after the occurrence data using the species names as a search term for the duckduckgo search engine library in Python as a separate csv file.

# Transformation (file 3)

The bird data was converted to a pandas dataframe and transformed by cleaning and editing the contents of certain columns (E.g.location information). 

# Loading (with basic profiling and exploratory analysis of data) (file 4 & 5)

After editing, data (bird details, image urls) were loaded (locally) to a postgreSQL database using sqlalchemy and pandas as two separate tables

Basic profiling and EDA was carried out to observe some trends and aggregates.

# Visualization (file 6 and image )

The database was used for creating a dashboard (power BI report) to visualize the interesting trends in the data based on the EDA observations. 
Since a public version of PoweBI was used,a screenshot of the dashboard has been shared instead of a link.

The project is still in progess with regards to data cleaning and exploration. A task scheduling and automation of this process is being worked out

*The API key and Database connection details have been removed from the script.File paths subject to change


 