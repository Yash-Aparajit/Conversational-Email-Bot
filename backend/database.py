# database.py
"""
A Python dictionary to temporarily store email data
Key: email_id (unique identifier), Value: email data (dictionary)
"""
#Creating a global dict
emails_db = {}
"""
Here I have created a global dictionary named emails_db. This acts like a temporary database. 
The key here, is the email ID, and the value will be the email content.
"""

# save a incoming email 
def save_email(email):
    email_id = email["email_id"]   # This provides us with a unique identifier by fetching the email_id from the email
    emails_db[email_id] = email  # Stores the email in the emails_db dictionary using email_id as the key.
    return email_id # Return the ID for reference.

def search_emails(sender=None, recipient=None, keyword=None): # None are default values.
    """
    It Searches for emails in the in database based on the filters: sender, recipient, and keyword (in subject or body).

    Parameters:
    - sender (str): Email address of the sender to filter results.
    - recipient (str): Email address of the recipient to filter results.
    - keyword (str): A word to search for in the subject or body of the email.

    Returns:
    - list: A list of email dictionaries that match the given inputs.
    """
    print(f"🔍 Searching for: sender={sender}, recipient={recipient}, keyword={keyword}") # Used to find what is input given by user.
    results = []  # Creats a empty list to store results.

    for email_id, email in emails_db.items():  # Checks through each stored email in the dictionary.
        print(f"Checking email: {email}")
        match = True # By default assumes that all email matches our filters 

        if sender and sender.lower() not in email["sender"].lower(): # Filter by sender
            match = False

        if recipient and recipient.lower() not in email["recipient"].lower(): # Filter by recipient
            match = False

        if keyword:   # Filter by keyword it check's that keyword is in subject or body
            keyword_lower = keyword.lower()
            subject_match = keyword_lower in email["subject"].lower()
            body_match = keyword_lower in email["body"].lower()
            if not (subject_match or body_match):
                match = False

        if match:
            results.append(email) # It add's the email to the results list.

    print(f"✅ Results: {results}")  # Print the final matched emails
    return results

