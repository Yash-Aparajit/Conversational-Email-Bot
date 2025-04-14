from pydantic import BaseModel
from typing import Optional

class Email(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str

class Reply(BaseModel):
    email_id: str
    sender: str
    body: str