import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Romeo@1715'
)

cursorObj = database.cursor()
cursorObj.execute("create database if not exists djangocrm")
print("done!")