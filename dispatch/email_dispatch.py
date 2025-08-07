import smtplib
from email.mime.text import MIMEText
from .base_dispatch import NewsDispatcher

class EmailDispatcher(NewsDispatcher):
    def __init__(self, sender_email, password, recipient_email, smtp_server='smtp.gmail.com', port=587):
        self.sender_email = sender_email
        self.password = password
        self.recipient_email = recipient_email
        self.smtp_server = smtp_server
        self.port = port

    def dispatch(self, report):
        try:
            msg = MIMEText(report, 'plain', 'utf-8')
            msg['Subject'] = 'Your News Report'
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email

            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)

            print(f"Report sent to {self.recipient_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")
