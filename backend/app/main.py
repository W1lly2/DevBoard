from fastapi import FastAPI, HTTPException

from repositories.user import get_user_by_id

app = FastAPI()

#Health check endpoint
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

#Endpoint to get user by ID
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        # User not found exception
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user[0],
        "user_name": user[1],
        "user_email": user[2]
    } 