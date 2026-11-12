"""
Assignment 4: Port management
Create this list:
ports = [5432, 1521, 3306, 1522, 5432, 1521]

Requirements:
1. Count how many times 1521 occurs.
2. Find the index of 3306.
3. Sort ports in ascending order.
4. Sort ports in descending order.
5. Reverse the original ordering using a separate list.
"""

ports = [5432, 1521, 3306, 1522, 5432, 1521]
revs_ports = ports.copy()
print(f"Ports: {ports}")
print(f"Count of 1521: {ports.count(1521)}")
print(f"The index of 3306: {ports.index(3306)}")
ports.sort()
print(f"Sort ports in ascending order: {ports}")
ports.sort(reverse=True)
print(f"Sort ports in descending order: {ports}")
revs_ports.reverse()
print(f"Reverse the original ordering using a separate list: {revs_ports}")