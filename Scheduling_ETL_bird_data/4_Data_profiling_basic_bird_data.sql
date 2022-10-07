      										----- Basic Data Profiling of the birds dataset -----


---1. Obtaining the data types of different fields in the dataset

select 
column_name,
data_type
from
information_schema.columns
where table_name = 'birds_data'
;

 
---2. Total row counts having non-null values in the data


select
sum(case when obs_date is not null then 1 else 0 end) as date_not_null_count,
sum(case when common_name is not null then 1 else 0 end) as common_sp_not_null_count,
sum(case when scientific_name is not null then 1 else 0 end) as sci_names_not_null_count,
sum(case when locality is not null then 1 else 0 end) as locality_not_null_count
FROM birds_data;


-- There are no null values in the dataset ----


---3. Distinct counts of some important fields 


select
count(distinct locality) as localities,
count(distinct common_name) as species_number
from
birds_data
;