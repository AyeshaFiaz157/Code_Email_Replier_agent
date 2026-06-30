import re
import smtplib
from email.mime.text import MIMEText


def parse_subject_body(draft: str) -> tuple[str, str]:
    """Extract subject and body from CrewAI output."""
    subject_match = re.search(r"^Subject:\s*(.+)$", draft, re.MULTILINE | re.IGNORECASE)
    if subject_match:
        subject = subject_match.group(1).strip()
        body = draft[subject_match.end() :].strip()
    else:
        subject = "Quick introduction"
        body = draft.strip()
    return subject, body


def send_reply(
    from_email: str,
    app_password: str,
    to_email: str,
    subject: str,
    body: str,
    smtp_host: str = "smtp.gmail.com",
    smtp_port: int = 587,
) -> None:
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
