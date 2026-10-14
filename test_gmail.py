
from pathlib import Path

from gmail_services import get_gmail_service
from gmail_sender import send_email

BASE = Path(__file__).parent

service = get_gmail_service()

recipient = input("Your own test email address: ").strip()
subject = (BASE / "subject.txt").read_text(
    encoding="utf-8"
).strip()
html = (BASE / "promotion.html").read_text(
    encoding="utf-8"
)

print(f"Test recipient: {recipient}")
print(f"Subject: [TEST] {subject}")

if input("Type TEST to send this test email: ") != "TEST":
    print("Cancelled.")
    raise SystemExit

try:
    message_id = send_email(
        service,
        recipient,
        "[TEST] " + subject,
        html,
        "DZ",
    )
    print("Gmail accepted the message.")
    print("Message ID:", message_id)
except Exception as exc:
    print("Send failed:", type(exc).__name__, str(exc))
