import os
from supabase import create_client

url = "Your Project URL"
key = "Your API KEy"

supabase = create_client(url, key)

response = supabase.table("Your Table Name").select("*").execute() ## * Mean all Column, If you want to Specifi ccolumn then Write like "Emp", "Salary" 
print(response)
