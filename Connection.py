import psycopg2

def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname="IMDb_Title",
            user="postgres",
            password="DKBLV1993",
            host="localhost",
            port="5431"
        )
        print("Verbindung zur Datenbank hergestellt.")

        return connection
    except Exception as e:
        print("Fehler beim Herstellen der Verbindung zur Datenbank:", e)
        return None

#valid_tablenames: akas , basics, crew, episode , principals, ratings
def select_from_table(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Fehler beim Ausführen der Abfrage:", e)

# Verbindung zur Datenbank herstellen,
# Outprint von AKAS-Tabelle ist auskommentiert, Outprint dauert ewig, ist aber keine Endlosloop

if __name__ == '__main__':

    db_connection = connect_to_database()

    if db_connection is not None:
        select_from_table(db_connection, "akas")

