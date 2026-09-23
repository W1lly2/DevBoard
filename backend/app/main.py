from fastapi import FastAPI, HTTPException, Depends, Header, Response, Cookie
import secrets
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from repositories.user import get_user_by_name

from services.auth import create_access_token, decode_access_token

app = FastAPI()

# Create a password hasher instance using BcryptHash
password_hasher = PasswordHash((BcryptHasher(),))

# Define a Pydantic model for the login request
class LoginRequest(BaseModel):
    user_name: str
    user_password: str

# Function to get the current user from the access token
async def get_current_user(
        access_token: str | None = Cookie(
            default=None, alias="access_token"
        )
    ):

    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    payload = decode_access_token(access_token)
    user_id = payload.get("sub")
    username = payload.get("username")

    # Validate user_id and raise an HTTPException if it is None
    if user_id is None:
        raise HTTPException(status_code=401, detail=("Invalid token"))

    return {
        "user_id": int(user_id),
        "username": username
    }

async def validate_csrf(
        csrf_cookie: str | None = Cookie(
            default = None,
            alias = "csrf_token"
        ),
        csrf_header: str | None = Header(
            default = None,
            alias = "X-CSRF_Token"
        ),      
):
    # Validate the CSRF token by comparing the value from the cookie and the header
    if csrf_cookie is None:
        raise HTTPException(status_code=403, detail="Missing CSRF cookie")
    if csrf_header is None:
        raise HTTPException(status_code=403, detail="Missing CSRF header")
    if not secrets.compare_digest(csrf_cookie, csrf_header):
        raise HTTPException(status_code=403, detail="Invalid CSRF token")

#Health check endpoint
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# CORS configuration for frontend connection
origins = [
    "http://localhost:5173"
]

# CORS middleware configuration that allows all origins, methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Endpoint to get user by ID
@app.get("/users/{user_name}")
async def read_user(user_name: str):
    user = get_user_by_name(user_name)
    if user is None:
        # User not found exception
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user[0],
        "username": user[1],
        "useremail": user[2]
    } 

@app.post("/login")
async def login(credentials: LoginRequest, response: Response):
    user = get_user_by_name(credentials.user_name)
    # Validate if the user exists, if not raise an HTTPException
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Get the stored password from the user record
    stored_password = user[3] 

    # Validate the provided password against the stored password using the password hasher
    if not password_hasher.verify(credentials.user_password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create an access token for the authenticated user
    token = create_access_token(user_id=user[0], username=user[1])

    # Generate a CSRF token for the session
    csrf_token = secrets.token_urlsafe(32)

    response.set_cookie(
        key="access_token", 
        value=token, 
        httponly=True, 
        secure=False,  # Set to True in production for HTTPS
        samesite="lax",
        path="/"
    )

    response.set_cookie(
        key="csrf_token",
        value=csrf_token,
        httponly=False,
        secure=False,
        samesite="lax",
        path="/"
    )

    return {
        "message": "Login succesfull"
    }

@app.get("/me")
async def get_me(user: int = Depends(get_current_user)):
    return user
