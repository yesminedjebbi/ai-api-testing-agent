
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="User Management API",
    description="Demo API for AI API Testing Agent",
    version="1.0.0"
)

# Base de données temporaire
users = {}
next_id = 1


# Structure d'un utilisateur
class UserCreate(BaseModel):
    name: str
    email: EmailStr


# GET /
@app.get("/")
def home():
    return {"message": "AI API Testing Agent"}


# GET /users
@app.get("/users")
def get_users():
    return list(users.values())


# POST /users
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    global next_id

    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email
    }

    users[next_id] = new_user
    next_id += 1

    return new_user


# GET /users/{id}
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[user_id]


# DELETE /users/{id}
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    del users[user_id]
