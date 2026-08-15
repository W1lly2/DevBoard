from app.database import get_connection

# Function that gets a user by ID from database
def get_user_by_id(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, user_name, user_email " \
            "FROM users WHERE user_id = %s", (user_id,))
            user = cur.fetchone()
            return user
