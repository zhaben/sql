# -*- coding: utf-8 -*-
"""Subscriber ID/Contact Identity Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PcO0RhxuEwDeN9SCAULitUj9hrXf0LAI

Subscriber ID - Contact Identity Test

Integration:Athena Purpose:Contact Identity
"""

with x as (
select
  emailaddress as email
, id as user_id
, createddate
, row_number() over(partition by emailaddress order by createddate desc) as user_id_rank
from contact_identity_datalake d
left join exacttarget_subscribers s
  on s.emailaddress = d.email
)

select email, user_id
from x
where user_id_rank = 1