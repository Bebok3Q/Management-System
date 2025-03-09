import os
from dotenv import load_dotenv
import psycopg2

load_dotenv('config/.env')

def load_db_config():
    db_config = {
        "type": os.getenv("DB_TYPE"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "name": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    return db_config

def get_db_conn():
    
    try: 
        conn = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        cursor = conn.cursor()
        print("Connected.")
    except Exception as e:
        print("Error while connecting", e)
# finally:
#     if (conn):
#         cursor.close()
#         conn.close()
#         print("Conn closed")
get_db_conn()