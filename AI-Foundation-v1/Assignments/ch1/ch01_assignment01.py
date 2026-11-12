"""
Assignment 1: Basic database information
Difficulty: Beginner

Create a Python program that stores the following information:
Variable	Value	Expected type
database_name	ORCL	str
server_name	oracle-prod-01	str
server_ip	192.168.1.10	str
database_port	1521	int
cpu_usage	75.5	float
memory_usage	82.3	float
database_running	True	bool

Requirements:
1. Create all seven variables.
2. Print every variable.
3. Print the data type of every variable.
4. Use meaningful variable names.
5. Do not hardcode the data types in the output. Use type().
Expected output structure:
DATABASE INFORMATION

Database Name: ORCL
Server Name: oracle-prod-01
Server IP: 192.168.1.10
Database Port: 1521
CPU Usage: 75.5
Memory Usage: 82.3
Database Running: True

DATA TYPES

<class 'str'>
<class 'str'>
...
"""
database_name = "ORCL"
server_name = "oracle-prod-01"
server_ip = "192.168.1.10"
database_port = 1521
cpu_usage = 75.5
memory_usage = 82.3
database_running = True

print("DATABASE INFORMATION\n")

print(f"Database Name: {database_name}")
print(f"Server Name: {server_name}")
print(f"Server IP: {server_ip}")
print(f"Database Port: {database_port}")
print(f"CPU Usage: {cpu_usage}")
print(f"Memory Usage: {memory_usage}")
print(f"Database Running: {database_running}")

print("DATA TYPES\n")

print(type(database_name))
print(type(server_name))
print(type(server_ip))
print(type(database_port))
print(type(cpu_usage))
print(type(memory_usage))
print(type(database_running))