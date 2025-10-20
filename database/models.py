from .connection import get_connection

# Create DB table
def create_conversation_table():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                        CREATE TABLE IF NOT EXISTS conversations (
                        id SERIAL PRIMARY KEY,
                        user_message TEXT NOT NULL,
                        ai_response TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                conn.commit()
                print("Table conversation ready to use")

    except Exception as e:
        print("Table creation error:",e)