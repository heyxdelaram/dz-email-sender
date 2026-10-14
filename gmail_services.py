
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

BASE = Path(__file__).parent
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def get_gmail_service():
    credentials = None
    token_path = BASE / "token.json"
    client_path = BASE / "credentials.json"

    if token_path.exists():
        credentials = Credentials.from_authorized_user_file(
            str(token_path), SCOPES
        )

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            if not client_path.exists():
                raise FileNotFoundError(
                    "Download your OAuth Desktop credentials "
                    "and save them as credentials.json."
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                str(client_path), SCOPES
            )
            credentials = flow.run_local_server(port=0)

        token_path.write_text(
            credentials.to_json(), encoding="utf-8"
        )

    service = build(
        "gmail", "v1", credentials=credentials
    )

    return service
