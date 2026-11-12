"""
Assignment 4: DBA monitoring configuration
Create a configuration for two database servers.

Server 1:
- Name: ORACLE-PROD
- Port: 1521
- CPU: 78.5
- Running: True
Server 2:
- Name: POSTGRES-PROD
- Port: 5432
- CPU: 65.2
- Running: False
Print each server's information and identify the data type of each value.
"""

database_name_1 = "ORACLE-PROD"
port_1 = 1521
cpu_1 = 78.5
running_1 = True

database_name_2 = "POSTGRES-PROD"
port_2 = 5432
cpu_2 = 65.2
running_2 = False

print("Server1")
print(f"Name: {database_name_1} Type: {type(database_name_1)}")
print(f"Port: {port_1} Type: {type(port_1)}")
print(f"CPU: {cpu_1} Type: {type(cpu_1)}")
print(f"Running: {running_1} Type: {type(running_1)}")

print("Server2")
print(f"Name: {database_name_2} Type: {type(database_name_2)}")
print(f"Port: {port_2} Type: {type(port_2)}")
print(f"CPU: {cpu_2} Type: {type(cpu_2)}")
print(f"Running: {running_2} Type: {type(running_2)}")

