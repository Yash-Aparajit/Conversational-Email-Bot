# Importing the Libraries

# FastAPI is the main framework
from fastapi import FastAPI, HTTPException
# Pydantic is used to define data models
from pydantic import BaseModel, Field
# These are Python standard data type
from typing import List, Optional
# uuid4() generates a unique ID
from uuid import uuid4


app = FastAPI() # Creating the FastAPI app instance



emails_db = [] # Memory storage for emails



# Defining the Email data model using Pydantic
class Email(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str
    email_id: str = Field(default_factory=lambda: str(uuid4()))  # Automatically generated email ID


# Keywords that trigger's the auto response
AUTO_REPLY_KEYWORDS = ["job", "opening", "interview", "resume", "job application"]

# Preset for auto response 
AUTO_REPLY_MESSAGE = "Thank you for reaching out. We will get back to you regarding your query."

@app.post("/send-email") # POST endpoint to send an email
def send_email(email: Email):
    """
    Receives a new email, stores it in the database, and checks if it should trigger an auto-reply.
    """
    print(f"📨 Received email from {email.sender} to {email.recipient}: {email.subject}")

    # Add to database 
    emails_db.append(email)  # Adds the auto-generated reply to your in-memory email database.
    print("✅ Email saved with ID:", email.email_id)

    # Check for keywords to trigger auto-reply
    combined_text = f"{email.subject} {email.body}".lower()
    if any(keyword in combined_text for keyword in AUTO_REPLY_KEYWORDS):
        auto_reply = Email(
            sender=email.recipient,
            recipient=email.sender,
            subject="Re: " + email.subject,
            body=AUTO_REPLY_MESSAGE,
        )
        emails_db.append(auto_reply)
        print(f"🤖 Auto-reply sent to {auto_reply.recipient}")

    return {"message": "Email sent successfully", "email_id": email.email_id}

@app.get("/get-emails", response_model=List[Email])  # GET endpoint to search emails
def get_emails(sender: Optional[str] = None, recipient: Optional[str] = None, keyword: Optional[str] = None):
    """
    Returns a list of emails filtered by optional sender, recipient, or keyword.
    """
    print(f"🔍 Searching for: sender={sender}, recipient={recipient}, keyword={keyword}")

    results = emails_db  # all emails are to be returned
    if sender:
        results = [email for email in results if email.sender == sender] #Only keep emails where the sender matches
    if recipient:
        results = [email for email in results if email.recipient == recipient] #Only keep emails where the recipient matches
    if keyword:
        keyword_lower = keyword.lower()
        results = [email for email in results if keyword_lower in email.subject.lower() or keyword_lower in email.body.lower()] #Only keep emails where the keyword matches

    print(f"✅ Results: {results}")  # Print matched emails to console
    return results
