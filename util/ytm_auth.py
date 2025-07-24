import os

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from util.ytm_log import setup_logger

SCOPES = ["https://www.googleapis.com/auth/youtube"]
TOKEN_FILE = "credentials/token.json"
CLIENT_SECRETS_FILE = "credentials/client_secret.json"

logger = setup_logger(__name__)


# Authenticate and return a YouTube service object
def authenticate_youtube():
    creds = None
    try:
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRETS_FILE, SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
    except Exception as e:
        logger.error(f"Authentication failed: {e}")
        raise

    youtube = build("youtube", "v3", credentials=creds)
    logger.info("YouTube authentication successful.")
    return youtube
