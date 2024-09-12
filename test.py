import mysql.connector
from mysql.connector.aio.charsets import charsets

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='country and airport',
    user='root',
    password='Hwhyll20180922@',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)