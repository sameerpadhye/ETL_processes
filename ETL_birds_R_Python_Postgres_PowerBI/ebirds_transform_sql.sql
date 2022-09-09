select
* 
from 
birds_data
limit 25
;

ALTER TABLE public.bird_data_tranform RENAME COLUMN "sciName" TO scientific_name;
ALTER TABLE public.bird_data_tranform RENAME COLUMN "locName" TO locality;
ALTER TABLE public.bird_data_tranform RENAME COLUMN lat TO latitude;
ALTER TABLE public.bird_data_tranform RENAME COLUMN lng TO longitude;
ALTER TABLE public.bird_data_tranform RENAME COLUMN "obsDt" TO obs_date;
ALTER TABLE public.bird_data_tranform RENAME COLUMN "comName" TO common_name;


select
* 
from 
bird_data_tranform
limit 25
;

--
update bird_data 
set "Identity" = 'Id_not_available'
where "Identity" is null
;
--

--
update bird_data 
set "Identity" = trim("Identity")
;
--

update bird_data 
set "OBSERVATION.COUNT" = null
where "OBSERVATION.COUNT" = 'X'
;

select 
length("OBSERVATION.COUNT")
from 
bird_data
where length("OBSERVATION.COUNT") is not null
;

alter table bird_data 
alter column "OBSERVATION.COUNT" type BIGINT using "OBSERVATION.COUNT"::BIGINT
;

select 
*
from
information_schema.columns
where table_name = 'bird_data'
;

select
count(*) not_approved
from
bird_data
where 
"APPROVED" is null
;

--to_date(trim(split_part(obs_date,'/',3)||'/'||split_part(obs_date,'/',1)||'/'|| split_part(obs_date,'/',2)),'YYYY/MM/DD') as obs_date