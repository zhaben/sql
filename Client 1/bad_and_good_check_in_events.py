# -*- coding: utf-8 -*-
"""BAD and Good Check-in Events.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLU5MrePhvxxyj2LhmlmBDbfANDvUyCi

BAD and Good Check-in Events

Integration:Amazon Redshift Purpose:Contact Event Data
"""

/* 
This dataset is similar to the main check-in dataset, except that it includes "bad check-ins". 
Equinox wants to consider all checkins when sending out communications to people who might have been at the club during the time that someone later tested positive for covid.
Good check-in, a valid check-in (scan successful)
Bad check-in, an invalid check-in (ex. overdue bill, former member)
*/

/* bring in all checkin-in data with checkin_status field to differentiate between both good and bad checkins 
  note the checkin_date and checkin_ts_local_time are in local time and are more reliable than the UTC timestamp (checkin_ts_time) per discussion with Casey McGowan (EQX)
*/
select member_id, 
facility_name, 
facility_code, 
checkin_status, 
date_part('epoch', checkin_ts_time)::int as checkin_datetime_UTC,
date_part('epoch', checkin_date)::int as checkin_date_local,
cast((substring(checkin_local_time,1,charindex(':',checkin_local_time)-1))||(substring(checkin_local_time,charindex(':',checkin_local_time)+1,len(checkin_local_time))) as int) as checkin_local_time,
md5(cast(member_id as varchar) || facility_name || cast(checkin_ts_time as varchar) || checkin_status) AS unique_id
from simon.event_all_checkins
where date_part('epoch', checkin_ts_time)::int > date_part('epoch', '2020-06-10 15:31:05')::int
--where date_part('epoch',checkin_ts_time)::int > 1593204338