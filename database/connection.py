import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

def get_connection():
    """DB connection using psycopg3"""
    try:
        conn=psycopg.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print("Database connection error:",e)
        raise