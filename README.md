# Daily Email Report Scheduler

This Python script automates the process of sending a daily email report at a specified time using the `smtplib` and `schedule` libraries.

## Features

- Sends a daily email with a report
- Configurable SMTP server and email account
- Uses `schedule` library for timing the report generation and email sending

## Technologies Used

- Python 3.x
- `smtplib` for email sending
- `email.mime.multipart.MIMEMultipart` and `email.mime.text.MIMEText` for email content creation
- `schedule` for task scheduling
