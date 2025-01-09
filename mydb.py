import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    username='root',
    password='Nas@3137_shah',
    database='crmbuild'
)
# super user: admin pwd: adminsystem
my_cursor = conn.cursor()

my_cursor.execute("DROP TABLE CUSTOMERS")

conn.commit()

conn.close()

print("Connection Success!")

