from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from repositories.user import get_user_by_name

app = FastAPI()

# Create a password hasher instance using BcryptHash
password_hasher = PasswordHash((BcryptHasher(),))

# Define a Pydantic model for the login request
class LoginRequest(BaseModel):
    user_name: str
    user_password: str

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
async def login(credentials: LoginRequest):
    user = get_user_by_name(credentials.user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Get the stored password from the user record
    stored_password = user[3] 

    if not password_hasher.verify(credentials.user_password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login succesfull",
        "userid": user[0],
        "username": user[1]
    }
