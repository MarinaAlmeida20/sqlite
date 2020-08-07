import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a Table
c.execute("SELECT rowid, * FROM customers")
#print(c.fetchone()[0])
#print(c.fetchmany(3))
items = c.fetchall()

for item in items:
    print(item)



#print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()