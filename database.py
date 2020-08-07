import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the Database - ORDER BY 
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

items = c.fetchall()

for item in items:
    print(item)




#print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()