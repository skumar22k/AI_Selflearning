"""
Assignment 3: Database decommissioning
Create a list containing five database names.

Requirements:
1. Remove one database using remove().
2. Remove the last database using pop().
3. Print the removed database.
4. Print the remaining databases.
"""

databases = ["PROD","UAT","DEV","SIT","QA"]
print(f"Databases: {databases}")
databases.remove("UAT")
print(f"databases.remove(\"UAT\") : {databases}")
pop_out_database = databases.pop(-1)
print(f"Removed last database: {pop_out_database}")
print(f"After removed : {databases}")