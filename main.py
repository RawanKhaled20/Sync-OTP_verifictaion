import random
import smtplib

#create a random number of 6 digits
def generate_otp():
    return str(random.randint(100000, 999999))


def send_email(email, otp):
    smtp_server = 'smtp.gmail.com'  # SMTP server for Gmail
    smtp_port = 587  # SMTP port for TLS
    sender_email = 'rk0905543@gmail.com'
    sender_password = 'inyl qjyh ejuk vwpv'

    # Create an SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to your email account
    server.login(sender_email, sender_password)

    # Compose the email
    subject = 'OTP Verification'
    message = f'Your OTP is: {otp}'
    msg = f'Subject: {subject}\n\n{message}'

    # Send the email
    server.sendmail(sender_email, email, msg)

    # Close the SMTP server
    server.quit()

# Generate OTP
otp = generate_otp()

user_email = input("Enter your email address: ")
send_email(user_email, otp)

user_entered_otp = input("Enter the OTP you received: ")

# Compare user_entered_otp with the generated otp
if user_entered_otp == otp:
    print("OTP is valid. Registration is successful!")
else:
    print("Invalid OTP. Registration failed.")

