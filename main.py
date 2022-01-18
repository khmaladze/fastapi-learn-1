from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("0b860234-ccf6-4345-9877-053774a15d3f"),
        first_name="test",
        last_name="test",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("9b0cc073-40fb-4f97-b721-29fb40ea845f"),
        first_name="test",
        last_name="test",
        gender=Gender.male,
        roles=[Role.student]
    )
]

@app.get("/api/v1/users")
async def fetch_users():
    return  db;

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
