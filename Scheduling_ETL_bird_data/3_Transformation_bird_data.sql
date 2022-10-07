                                         ----- Data Transformation of bird data -----


-- Look at the original data

select
* 
from 
birds_data_daily
;

-- Alter column names

ALTER TABLE public.bird_data_tranform RENAME COLUMN "sciName" TO scientific_name;

ALTER TABLE public.bird_data_tranform RENAME COLUMN "locName" TO locality;

ALTER TABLE public.bird_data_tranform RENAME COLUMN lat TO latitude;

ALTER TABLE public.bird_data_tranform RENAME COLUMN lng TO longitude;

ALTER TABLE public.bird_data_tranform RENAME COLUMN "obsDt" TO obs_date;

ALTER TABLE public.bird_data_tranform RENAME COLUMN "comName" TO common_name;


-- Replacing the null values in species columns to 'Id_not_available'

update birds_data_daily  
set scientific_name = 'Id_not_available'
where scientific_name is null
;

-- Trim spaces if/any from the species name column

update birds_data_daily 
set scientific_name = trim(scientific_name)
;

-- Converting the first alphabet into upper case in the name column

update birds_data_daily 
set scientific_name = initcap(scientific_name) 


-- Trim spaces if/any from the locality column

update birds_data_daily 
set locality = trim(locality)
;

-- Converting the first alphabet into upper case in the locality column

update birds_data_daily 
set locality = initcap(locality) 


-- Remove the numbers from locality column

update birds_data_daily
set locality = regexp_replace(trim(regexp_replace(locality,'[[:digit:]]+','')),'/[[:digit:]]','')
;

-- Converting the count data given as 'X' to null value

update bird_data 
set "OBSERVATION.COUNT" = null
where "OBSERVATION.COUNT" = 'X'
;

-- Convert the Count data to Integer data

alter table bird_data 
alter column "OBSERVATION.COUNT" type BIGINT using "OBSERVATION.COUNT"::BIGINT
;

-- Updating locality data where exact information is not known

update birds_data_daily
set locality = regexp_replace(locality,'\((.+)\)','')
where locality ~'\((.+)\)'
;