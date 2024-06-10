import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # For TL .
EMAIL_ADDRESS = 'ah.hamdi.mohi@gmail.com'
EMAIL_PASSWORD = '*********'

# Function to create email content
def create_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

