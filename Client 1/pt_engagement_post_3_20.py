# -*- coding: utf-8 -*-
"""PT engagement post 3/20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jfEA8Z87WE9nrnXAk85YyQf6-x1iddRc

PT engagement post 3/20

Integration:Amazon Redshift Purpose:Contact Data
"""

/* identify if members have taken PT since 3/20/20 as part of COVID analysis */
with boolean_cte as (
select member_id, 
last_used_paid_pt_date as pt_after_3_20,
case when cast(last_used_paid_pt_date as date) > '2020-03-20' then true else false end as is_pt_after_3_20
from member_personal_training
)

/* output a boolean field for each member id to indicate if PT were taken ater 3/20/20 */
select member_id, 
is_pt_after_3_20 
from boolean_cte