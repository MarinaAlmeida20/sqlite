import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a Table
c.execute("SELECT * FROM customers")
print(c.fetchone()[0])
#print(c.fetchmany(3))
#print(c.fetchall())




#print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()