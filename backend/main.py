import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

load_dotenv(Path(__file__).with_name(".env"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://portfolio-saachi.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.get("/")
def home():
    return {"message": "Portfolio backend is running!"}

@app.post("/contact")
def send_contact_message(contact: ContactMessage):
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_APP_PASSWORD")
    receiver = os.getenv("CONTACT_RECEIVER")

    if not smtp_email or not smtp_password or not receiver:
        raise HTTPException(
            status_code=500,
            detail="Email configuration incomplete."
        )

    email = EmailMessage()
    email["Subject"] = f"Portfolio contact form {contact.name}"
    email["From"] = smtp_email
    email["To"] = receiver
    email["Reply-To"] = str(contact.email)

    email.set_content(
        f"""
You revieved a new message through your portfolio.

Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(smtp_email, smtp_password)
            server.send_message(email)

    except (smtplib.SMTPException, OSError):
        raise HTTPException(
            status_code=502,
            detail="The email could not be sent. Please try again later."
        )

    return {"message": "Your message was emailed successfully!"}
