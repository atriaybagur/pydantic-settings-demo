import re
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")


@dataclass
class User:
    name: str
    email: str
    signup_date: date
    age: int
    website: Optional[str] = None

    @staticmethod
    def validate(payload: dict) -> "User":
        # manual type conversions
        name = str(payload["name"])
        email = str(payload["email"])
        if not EMAIL_RE.match(email):
            raise ValueError("email is not valid")

        signup_raw = payload.get("signup_date")
        if isinstance(signup_raw, str):
            signup_date = datetime.fromisoformat(signup_raw).date()
        elif isinstance(signup_raw, date):
            signup_date = signup_raw
        else:
            raise ValueError("signup_date must be ISO string or date")

        age = int(payload["age"])  # will raise if not int-like

        website = payload.get("website")
        if website is not None and not website.startswith(("http://", "https://")):
            raise ValueError("website must start with http:// or https://")

        return User(
            name=name, email=email, signup_date=signup_date, age=age, website=website
        )


payload = {
    "name": "Ada",
    "email": "ada@example.com",
    "signup_date": "2025-08-15",
    "age": "30",
    "website": "https://ada.com",
}
user = User.validate(payload)
print(user)
