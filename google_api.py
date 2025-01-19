from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar.events']

def authenticate_google():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def send_email(creds, recipient, subject, body):
    service = build('gmail', 'v1', credentials=creds)
    message = {
        'raw': base64.urlsafe_b64encode(
            f"To: {recipient}\nSubject: {subject}\n\n{body}".encode()
        ).decode()
    }
    service.users().messages().send(userId='me', body=message).execute()