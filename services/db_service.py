from database.connection import get_connection

def save_conversation(user_message:str,ai_response:str):
    """Save message and response into the DB"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO conversations (user_message, ai_response) VALUES (%s, %s)",
                    (user_message, ai_response))
                conn.commit()
                print("Conversation saved.")
                
    except Exception as e:
        print("Database save error:",e)