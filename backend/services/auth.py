import os 
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

import jwt

JWT_SECRET = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

# Function to create an access token
def create_access_token(user_id: int, username: str):
    expire = datetime.now(timezone.utc) + timedelta(hours=1)
    payload = {
        "sub": str(user_id),
        "username": username,
        "exp": expire
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

    return token

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
