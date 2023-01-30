from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText

load_dotenv()

context = ssl.create_default_context()
message = MIMEText("Test Email")
message['Subject'] = "Moreboard Notification"
message['From'] = os.getenv("MOREBOARD_EMAIL")
message['To'] = "treywesleydavis@gmail.com"
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(os.getenv("MOREBOARD_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail(os.getenv("MOREBOARD_EMAIL"), "treywesleydavis@gmail.com", message.as_string())
        print("Email sent")
except Exception as e:
    print(str(e))
