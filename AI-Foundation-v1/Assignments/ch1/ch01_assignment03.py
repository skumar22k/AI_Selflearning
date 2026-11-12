"""
Assignment 3: Database health information
Create variables for:
- Database name.
- Total sessions.
- Active sessions.
- CPU utilization.
- Memory utilization.
- Database availability.
Use appropriate Python data types.

Print all information and their data types.ii
"""
database_name = "ORCL"
total_sessions = 150
active_sessions = 120
cpu_utilization = 31.2
memory_utilization = 68.5
database_availablity = True

print(f"Database Name: {database_name} Type: {type(database_name)}")
print(f"Total Sessions: {total_sessions} Type: {type(total_sessions)}")
print(f"Active Sessions: {active_sessions} Type: {type(active_sessions)}")
print(f"CPU Utilization: {cpu_utilization} Type: {type(cpu_utilization)}")
print(f"Memory Utilization: {memory_utilization} Type: {type(memory_utilization)}")
print(f"Database Availablity: {database_availablity} Type: {type(database_availablity)}")