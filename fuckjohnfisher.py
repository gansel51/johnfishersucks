import smtplib
import time

# Email and login details
from_address = "griffin.ansel@gmail.com"
to_address = "john.fisher@athletics.com"
password = env.email_password

# SMTP server details for Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Message details
subject = "Fuck you, you garbage human being"
body = "Dear John Fisher, you took the A's from Oakland, and now you're not welcome here. Enjoy the desert, it's as barren as your heart."

while True:
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, password)

        # Construct the message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(from_address, to_address, message)

        # Close the connection to the server
        server.quit()

        # Wait for five minutes before sending the next email
        time.sleep(300)

    except Exception as e:
        print(f"Error: {e}")
