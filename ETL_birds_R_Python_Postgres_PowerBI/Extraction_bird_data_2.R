## Extraction of bird data using the rebird package ##

# The key which is required to access the data has been stored in a different file and sourced here

source("G:/Research data/Other groups/Ebird_data/ETL_birds_R_Python_Postgres_PowerBI/ebird_api_1.R")

# Installing and importing the rebird package

#install.packages('rebird')

library(rebird)

library(tidyverse)

# Defining the time frame for data download (max available is 6 months)

date_seq<-seq(as.Date("2022-01-01"), 
              as.Date("2022-07-31"), 
              1)
date_seq

# Function to obtain the bird data from Pune region, India

data_bird_fn<-function(x) {
  
  step_1 = ebirdhistorical(loc = "IN-MH-PU", 
                           date = x, 
                           fieldSet = 'full',
                           key=api_ebird)
  return(step_1)
}

# Obtaining the data 

bird_data<-lapply(date_seq,data_bird_fn)%>%
  bind_rows()

# Export the data as a csv

write.csv(bird_data,"G:/Research data/Other groups/Ebird_data/ETL_birds_R_Python_Postgres_PowerBI/bird_data_extraction.csv")
