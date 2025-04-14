# ai.py

def generate_ai_reply(email_body: str) -> str:

    """
    Generates an automated reply for emails if specific keywords are found in that input.
    The function expects a parameter called email_body & the function will return a string.
    """
    # Define Target keywords in form of list
    keywords = ["job", "opening", "interview", "resume", "application", "apply", "opportunity"]

    """
    The function scans the email body for job-related terms such as:
    'job', 'opening', 'interview', 'resume', 'application', 'apply', 'opportunity'.
    If any of these words are found, it assumes the email is job-related and sends
    an appropriate response.
    """

    # Convert the email body to lowercase to make the keyword search case-insensitive
    email_body_lower = email_body.lower()
    if any(keyword in email_body_lower for keyword in keywords):
        return (
            "Thank you for reaching out regarding job opportunities. "
            "We have received your application and our team will get back to you shortly."
        )
    
    return ""  
# Return an empty string if no relevant keywords are found
