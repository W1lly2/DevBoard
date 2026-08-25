from app.database import get_connection

# Function that gets a user by name from database
def get_user_by_name(user_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, user_name, user_email, user_password_hash " \
            "FROM users WHERE user_name = %s", (user_name,))
            user = cur.fetchone()
            return user
