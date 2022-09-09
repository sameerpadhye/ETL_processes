--------------------------------------- Basic profiling and Exploratory Analysis of data -----------------------------------------------------

-- Observe the dataset

select *
from 
birds_data
limit 10
;


---1. Obtaining the data types of different fields in the dataset

select 
column_name,
data_type
from
information_schema.columns
where table_name = 'birds_data'
;

---2. Checking whether there are null values in the whole dataset

select 
count(*) - count(locality)
from
birds_data
;

---3. Total row counts having non-null values in specific columns

select
sum(case when obs_date is not null then 1 else 0 end) as date_not_null_count,
sum(case when common_name is not null then 1 else 0 end) as common_sp_not_null_count,
sum(case when scientific_name is not null then 1 else 0 end) as sci_names_not_null_count,
sum(case when locality is not null then 1 else 0 end) as locality_not_null_count
FROM birds_data;

---4. Distinct counts of some important fields 

select
count(distinct locality) as localities,
count(distinct common_name) as species_number
from
birds_data
;

---5. Ranking the localities based on the count data 

select
locality,
sum(count) as counts,
count (locality) as locality_obs,
rank () over (order by sum(count)::numeric desc) as locality_rank
from 
birds_data
where count is not null
group by locality
;

---6. Ranking the species based on the average count data 

select 
common_name,
scientific_name ,
count(common_name) as counts,
row_number () over (order by round(avg(count)::numeric,2)::numeric desc) as species_rank,
round(avg(count)::numeric,2) as avg_counts_obs 
from
birds_data
group by 1,2
;

---7 Ranking the species based on the relative counts of species

select 
common_name,
count(locality) as loc_count,
round((sum(count)/count(locality))::numeric,3) rel_counts 
from
birds_data
where count is not null
group by 1
order by rel_counts desc
;

---8 Ranking the locations based on the their respective counts

select 
row_number () over (order by loc_counts desc) as rank,
locality,
loc_counts,
total_occ_sp,
round((total_occ_sp/loc_counts)::numeric,2)as rel_sp_to_loc_val
from (select 
locality,
sum(count) as total_occ_sp,
count(*) as loc_counts
from
birds_data
where count is not null
group by 1
order by loc_counts desc
) as subq
where total_occ_sp is not null
order by rank 
;
 
---9 Five most commonly seen species (location count wise)

select 
common_name,
count(common_name),
round(avg(count)::numeric,2) as avg_counts
from
birds_data
group by common_name
order by count desc 
limit 5
;

---10 Five most commonly seen species (species count wise)

select 
common_name,
sum(count) total_counts,
round(avg(count)::numeric,2) as avg_counts
from
birds_data
group by common_name
order by total_counts desc 
limit 5
;

---11 Five top localities for each bird species

with temp_table_rank as (
select 
common_name,
locality,
loc_counts,
total_occ_sp,
round((total_occ_sp/loc_counts)::numeric,2)as occ_to_loc_counts
from (select 
common_name,
locality,
sum(count) as total_occ_sp,
count(*) as loc_counts
from
birds_data
where locality not like '%Location name not known%'
group by 1,2
order by loc_counts desc
) as subq
where total_occ_sp is not null
order by occ_to_loc_counts desc
)
select 
common_name,
locality
from(select 
locality,
common_name,
loc_counts,
row_number () over (partition by common_name order by loc_counts desc) as rank
from 
temp_table_rank) as subq
where rank <=5
;

