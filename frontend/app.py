# Import necessary libraries
import streamlit as st
import requests

# Page setup (Frontend UI)
st.set_page_config(page_title="Conversational Email Bot", layout="centered")

# Main page title
st.title("📧 Conversational Email Bot (AI Job Assistant)")

# Backend URL
backend_url = "http://127.0.0.1:8000"


# 📤 Send Email Section
st.header("📤 Send Email")

# Using a Streamlit form for sending email
with st.form("email_form"):
    sender = st.text_input("Sender")
    recipient = st.text_input("Recipient")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    submitted = st.form_submit_button("Send Email")

# If form is submitted
    if submitted: 
        email = {      # Build email data as dictionary
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "body": body
        }
        response = requests.post(f"{backend_url}/send-email", json=email) # Displaying feedback based on the response status
        if response.status_code == 200:
            st.success("Email sent successfully!")
        else:
            st.error("Failed to send email.")

# Divider
st.markdown("---")


# 🔍 Search Emails Section
st.header("🔍 Search Emails")

# Using Streamlit form for searching emails
with st.form("search_form"):
    search_sender = st.text_input("Filter by Sender")
    search_recipient = st.text_input("Filter by Recipient")
    search_keyword = st.text_input("Keyword in Subject/Body")
    search_clicked = st.form_submit_button("Search")

    if search_clicked:
        # Construct query parameters
        params = {} # Building a dictionary that contains only the filters provided by the user.
        if search_sender:
            params["sender"] = search_sender
        if search_recipient:
            params["recipient"] = search_recipient
        if search_keyword:
            params["keyword"] = search_keyword

        st.write("Search Params:", params)  

        # Send GET request
        sts.get(f"{backeresponse = requend_url}/get-emails", params=params)


        # Send GET request
        response = requests.get(f"{backend_url}/get-emails", params=params)
        if response.status_code == 200:
            data = response.json()
            emails = data  #  API returns a list of emails directly

            if not emails:      # If no emails matched the filters
                st.warning("No emails found for this search.")
            else:
                for email in emails:
                    st.markdown("### 📩 Email")
                    st.markdown(f"**From:** {email['sender']}")
                    st.markdown(f"**To:** {email['recipient']}")
                    st.markdown(f"**Subject:** {email['subject']}")
                    st.markdown(f"**Body:** {email['body']}")

# If email has AI-generated replies 
                    if email.get("replies"):
                        st.markdown("**🤖 AI Replies:**")
                        for reply in email["replies"]:
                            st.markdown(f"- **{reply['sender']}**: {reply['body']}")
                    st.markdown("---")
        else: 
            st.error("Failed to fetch emails.")
