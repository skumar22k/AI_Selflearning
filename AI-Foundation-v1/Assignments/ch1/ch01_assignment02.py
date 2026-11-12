"""
Assignment 2: Database configuration conversion
Create these variables as strings:
port = "1521"
max_connections = "500"
cpu_usage = "85.75"



Requirements:
- Convert port to integer.
- Convert max_connections to integer.
- Convert cpu_usage to float.
- Print their values and types.
"""

port = "1521"
max_connections = "500"
cpu_usage = "85.75"

print(f"Port: {port}")
print(f"Max Connections: {max_connections}")
print(f"CPU Usage: {cpu_usage}")

port = int(port)
max_connections = int(max_connections)
cpu_usage = float(cpu_usage)

print(type(port))
print(type(max_connections))
print(type(cpu_usage))