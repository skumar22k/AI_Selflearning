"""
Assignment 5: DBA server inventory
Create a nested list:
servers = [    ["DB01", "ORCL", 1521],    ["DB02", "PROD", 1522],    ["DB03", "DEV", 1523]]

Requirements:
1. Print all server details.
2. Print only database names.
3. Change the second server's database name to PRODUCTION.
4. Add a fourth server.
5. Print the final inventory.
"""

servers = [ ["DB01", "ORCL", 1521], ["DB02", "PROD", 1522], ["DB03", "DEV", 1523]]

print(f"All server details: {servers}")
print(f"Only database names: {servers[0][1]},{servers[1][1]},{servers[2][1]}")

servers[1][1] = "PRODUCTION"

print(f"Change the second server's database name to PRODUCTION: {servers}")

servers.extend([["DB04","QA",1524]])

print(f"The final inventory: {servers}")