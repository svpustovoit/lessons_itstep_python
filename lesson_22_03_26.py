import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

#print(F"connection: {connection}")
#print(F"cur: {cur}")

#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
#cur.execute("INSERT INTO first_table (name) VALUES ('Sofia');")
#cur.execute("INSERT INTO first_table (name) VALUES ('John');")
#cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
#cur.execute("SELECT rowid, name FROM first_table rowid;")
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid=4;")
#cur.execute("SELECT rowid, name FROM first_table rowid;")
#cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=6")
cur.execute("SELECT rowid, name FROM first_table rowid;")
connection.commit()

result = cur.fetchall()
print(result)

connection.close()











