import pandas as pd
from supabase import create_client

# Supabase project details
url = "Projec URL"
key = "API-KEY"

# Create Supabase client
supabase = create_client(url, key)


# Delete rows where id is NOT NULL
try:
    delete_response = (
        supabase
        .table("Employee")
        .delete()
        .filter("id", "not.is", "null")  # Use `.filter()` for conditions
        .execute()
    )
    print("Data deleted where id is not null:", delete_response)
except Exception as e:
    print(f"Error during deletion: {e}")

# Path to the Excel file
excel_file_path = "data.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Ensure column names match your Supabase table fields
# For example: emp_id, emp_name, designation, Salary , Dept_id
for index, row in df.iterrows():
    # Prepare the row data as a dictionary
    row_data = {
        "id": row["emp_id"],  # Replace with the column name in your Excel file
        "emp_name": row["emp_name"],
        "designation": row["designation"],
        "Salary": row["Salary"],
        "Dept_id": row["Dept_id"]
    }
    
    # Insert row into Supabase table
    insert_response = supabase.table("doctor_info").insert([row_data]).execute()
    print(f"Row {index} inserted: {insert_response}")
