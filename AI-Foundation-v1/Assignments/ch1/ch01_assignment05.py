"""
Assignment 5: Mini project - DBA server inventory
Build a Python script representing three database servers.

Each server should have:
- Server name.
- Database type.
- IP address.
- Port.
- CPU usage.
- Memory usage.
- Availability status.
Requirements:
1. Store the information using individual variables for each server.
2. Use appropriate data types.
3. Display all server information.
4. Display the data type of each field.
5. Use readable output formatting.
"""
server_name_1 = "ORACLE-PROD01"
database_type_1 = "Oracle"
ip_address_1 = "192.168.1.10"
port_1 = 1521
cpu_usage_1 = 78.5
memory_usage_1 = 68.5
running_1 = True

server_name_2 = "PG-PROD01"
database_type_2 = "Postgresql"
ip_address_2 = "192.168.1.11"
port_2 = 5432
cpu_usage_2 = 65.2
memory_usage_2 = 75.0
running_2 = False

server_name_3 = "MySQL-PROD01"
database_type_3 = "MySQL"
ip_address_3 = "192.168.1.12"
port_3 = 3306
cpu_usage_3 = 70.0
memory_usage_3 = 80.0
running_3 = True


print(f"\nServer Name: {server_name_1} Type: {type(server_name_1)}")
print(f"Database Type: {database_type_1} Type: {type(database_type_1)}")
print(f"IP Address: {ip_address_1} Type: {type(ip_address_1)}")
print(f"Port: {port_1} Type: {type(port_1)}")
print(f"CPU Usage: {cpu_usage_1} Type: {type(cpu_usage_1)}")
print(f"Memory Usage: {memory_usage_1} Type: {type(memory_usage_1)}")
print(f"Running: {running_1} Type: {type(running_1)}")

print(f"\nServer Name: {server_name_2} Type: {type(server_name_2)}")
print(f"Database Type: {database_type_2} Type: {type(database_type_2)}")
print(f"IP Address: {ip_address_2} Type: {type(ip_address_2)}")
print(f"Port: {port_2} Type: {type(port_2)}")
print(f"CPU Usage: {cpu_usage_2} Type: {type(cpu_usage_2)}")
print(f"Memory Usage: {memory_usage_2} Type: {type(memory_usage_2)}")
print(f"Running: {running_2} Type: {type(running_2)}")

print(f"\nServer Name: {server_name_3} Type: {type(server_name_3)}")
print(f"Database Type: {database_type_3} Type: {type(database_type_3)}")
print(f"IP Address: {ip_address_3} Type: {type(ip_address_3)}")
print(f"Port: {port_3} Type: {type(port_3)}")
print(f"CPU Usage: {cpu_usage_3} Type: {type(cpu_usage_3)}")
print(f"Memory Usage: {memory_usage_3} Type: {type(memory_usage_3)}")
print(f"Running: {running_3} Type: {type(running_3)}")
