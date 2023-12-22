import psycopg2

def connect_to_db():
    try:
        # Configura los parámetros de conexión
        db_config = {
            'host': 'localhost',
            'database': 'transacciones_db',
            'user': 'postgres',
            'password': 'admin'
        }

        # Establece la conexión
        connection = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")
        return connection
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al conectar a PostgreSQL:", error)
        return None

# Obtener la conexión
connection = connect_to_db()

if connection:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print("Versión de PostgreSQL:", version)
        cursor.close()
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta:", e)
    finally:
        connection.close()