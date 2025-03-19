import mysql.connector


DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Chotujain@1234",
    "database": "gs"
}

def get_sql_connection():
    """Establishes a new MySQL connection for each request."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error connecting to MySQL: {err}")
        return None

if __name__ == '__main__':
    conn = get_sql_connection()
    if conn:
        print("✅ Connected to MySQL successfully!")
        conn.close() 
    else:
        print("❌ Connection failed!")
