"""
Assignment 1: Database inventory
Create a list containing five database names.

Requirements:
1. Print the complete list.
2. Print the first database.
3. Print the last database.
4. Change the second database name.
5. Print the updated list.
"""

databases = ["ORCL01", "PROD", "DEV", "UAT", "SIT" ]

print(f"Complete list: {databases}")
print(f"First database: {databases[0]}")
print(f"Last database: {databases[-1]}")
databases[1] = "PRODUCTION"
print(f"Updated list: {databases}")