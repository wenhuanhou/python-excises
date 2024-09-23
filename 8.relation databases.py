###1###
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

###2###
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
def get_airports_by_country(country, conn):
    cursor = conn.cursor()
    query = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type"
    cursor.execute(query, (country,))
    result = cursor.fetchall()
    cursor.close()
    return result

country_input = input("enter the country code (e.g. 'FI' for Finland): ").upper()

conn = connect_db()
airports = get_airports_by_country(country_input, conn)

if airports:
    print(f"airports in {country_input} by type:")
    for airport_type, count in airports:
        print(f"{airport_type}: {count}")
else:
    print(f"No airports found: {country_input}")

###3###
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
def airport_location(icao, conn):
    cursor = conn.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result

def calculate_distance(icao1, icao2, conn):
    location1 = airport_location(icao1, conn)
    location2 = airport_location(icao2, conn)
    print(location1)
    if location1 and location2:
        distance = geodesic(location1, location2).kilometers
        return distance
    else:
        return None

def main():
    icao1 = input("enter the first ICAO code: ")
    icao2 = input("enter the second ICAO code: ")

    conn = connect_db()
    distance = calculate_distance(icao1, icao2, conn)
    if distance is not None:
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("Not found one or the two airports.")

    conn.close()

if __name__ == '__main__':
    main()