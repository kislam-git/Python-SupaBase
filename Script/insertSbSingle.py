import os
from supabase import create_client

url = "prjectUrl"
key = "APIKEY"

supabase = create_client(url, key)

v_doc_id = 525
v_doc_name = "Name"
v_designation = "Professor"
v_speciality = "Medicine"
v_hospital = "Hospital Name"
v_doc_image_url = "imageUrl"
v_doc_degree = "MBBS, MD"


insert = supabase.table("doctor_info").insert([{
          "id" : v_doc_id, 
          "doctor_name": v_doc_name,
          "designation": v_designation,
          "speciality": v_speciality,
          "degree": v_doc_degree,
          "doc_image_url": v_doc_image_url,
          "hospital": v_hospital
          }]).execute()
print(insert)
