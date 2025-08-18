from datetime import date

from pydantic import BaseModel, EmailStr, HttpUrl, PositiveInt


class User(BaseModel):
    name: str
    email: EmailStr
    signup_date: date
    age: PositiveInt
    website: HttpUrl


user = User(
    name="Alice",
    email="alice@example.com",
    signup_date="2025-08-15",
    age=30,
    website="https://alice.com",
)
print(user)  # Print the user object
print(user.model_dump())  # Serialise output
