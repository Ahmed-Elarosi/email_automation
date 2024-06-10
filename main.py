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

# Function to send the email
def send_email(subject, body):
    msg = create_email(subject, body)
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to generate the daily report
def generate_daily_report():
    # Placeholder for report content; replace with actual data generation logic
    report_content = "This is your daily report content."
    send_email("Daily Report", report_content)

# Schedule the task to run daily at a specific time (e.g., 8 AM)
schedule.every().day.at("23:07").do(generate_daily_report)

# Main loop to keep the script running and checking the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
