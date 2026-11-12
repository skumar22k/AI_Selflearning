"""
Assignment 2: Database onboarding
Create an empty list called databases.

Requirements:
1. Add three databases using append().
2. Insert another database at index 1.
3. Add two more databases using extend().
4. Print the final list.
"""

databases = []

databases.append("PROD")
databases.append("UAT")
databases.append("QA")
databases.insert(1,"SIT")
databases.extend(["MO","STAGE"])
print(f"Final list: {databases}")
