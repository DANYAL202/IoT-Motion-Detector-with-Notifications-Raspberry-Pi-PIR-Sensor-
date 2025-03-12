import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

# Set up GPIO
PIR_PIN = 17  # Pin for PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Email setup
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "receiver_email@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_PASSWORD = "YourEmailPassword"

# Function to send email notification
def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

# Main program
try:
    print("System Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            send_email("Motion Alert", "Motion detected by PIR sensor.")
            time.sleep(10)  # Wait for 10 seconds before detecting motion again
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    GPIO.cleanup()
