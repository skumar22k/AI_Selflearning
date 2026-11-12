"""
Assignment 1: Database configuration
Create a tuple named db_config containing:
- Database name
- Environment
- Hostname
- Port
- Service name
Requirements:
1. Print the complete tuple.
2. Print its data type.
3. Print each element using indexing.
4. Unpack the tuple into five variables.
5. Print the unpacked variables individually.
Expected behavior: Correctly display all five configuration values.
"""
db_config = ("ORCL","DEV","oracledb-srv01",1521,"ORCLPDB01")

print(f"\nThe complete tuple: {db_config}")
print(f"\ndb_config data type: {type(db_config)}")
print(f"\nPrinting each element using indexing\n")
for i in range(len(db_config)):
   print(f"db_config [{i}]: {db_config[i]}")

database_name, environment, host_name, port, service_name = db_config
print(f"\nDatabase name: {database_name}\nEnvironment: {environment}\nHostname: {host_name} \nPort: {port} \nService name: {service_name}\n")