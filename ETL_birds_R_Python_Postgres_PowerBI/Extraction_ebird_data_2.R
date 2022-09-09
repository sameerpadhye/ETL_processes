## Extraction of bird data using the rebird package ##

# The key which is required to access the data is sourced here (Provide the path)

source("G:/.......")

# Installing and importing the rebird package

install.packages('rebird')

library(rebird)

# tidyverse package is used for data wrangling

require(tidyverse)

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

# Export the data as a csv (Provide the path where the file should be stored)

write.csv(bird_data,"G:/.....")
