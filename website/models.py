import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3336",
    user="root",
    passwd="MyNewPass"
)
cur = db.cursor()

database = cur.execute("SHOW DATABASES")
print(database)

def createAcft(cur):
    pass