from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, EmailStr
from typing import Optional
import asyncio

app = FastAPI()

class UserRegistrationRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

async def send_confirmation_email(email: str):
    # Simulate an I/O-bound operation (e.g., sending an email)
    await asyncio.sleep(2)  # Simulate delay for demonstration
    print(f"Confirmation email sent to {email}")

@app.post("/register")
async def register_user(
    request: UserRegistrationRequest
    # background_tasks: BackgroundTasks  # To be used as needed
):
    # Registration logic here (e.g., validate/email store user)
    # Email sending currently blocks response (to be refactored)
    await send_confirmation_email(request.email)
    return {"message": "User registered successfully. Confirmation email sent."}
