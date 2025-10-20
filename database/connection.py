import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
print(f"Attempting to connect to DATABASE_URL: {DATABASE_URL}")

# db connect function
def get_connection():
    try:
        conn=psycopg.connect(DATABASE_URL)
        print("Database connection successful.")
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        raise