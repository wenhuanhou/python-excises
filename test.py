import mysql.connector

def connect_db():
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
    return conn

def fetch_airport_info(icao_code):
    conn = connect_db()
    cursor = conn.cursor(buffered=True)

    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))


    result = cursor.fetchone()

    conn.close()
    return result

icao_code = input("enter the ICAO code：").strip().upper()
conn = connect_db()
airport_info = fetch_airport_info(icao_code)

if airport_info:
    airport_name, location = airport_info
    print(f"airport name: {airport_name}")
    print(f"city: {location}")
else:
    print(f"Not found the airport of'{icao_code}'")


