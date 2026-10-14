
import base64
from email.message import EmailMessage

from googleapiclient.errors import HttpError


def send_email(service, recipient, subject, html, sender_name):
    message = EmailMessage()
    message["To"] = recipient
    message["Subject"] = subject

    # Plain-text alternative
    message.set_content(
        "Please view this promotional email in an HTML-capable "
        "email client."
    )

    message.add_alternative(html, subtype="html")

    encoded = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode("utf-8")

    result = service.users().messages().send(
        userId="me",
        body={"raw": encoded},
    ).execute()

    return result["id"]
