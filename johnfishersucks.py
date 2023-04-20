import os
import smtplib
import time

# Email and login details
from_address = "griffin.ansel@gmail.com"
to_address = "john.fisher@athletics.com"
sender_name = "Griffin Ansel"
password = os.environ.get["email_password"]

# SMTP server details for Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Message details
subject = "John Fisher, We Hate You"
body = f"""Dear John Fisher,

On behalf of the City of Oakland, let me tell you that you are no longer welcome. Rooted in Oakland, what a joke.
You told us you would keep our team here, but instead you pull a "major league" and tank for a season, raise ticket and
concession prices, then complain when fans don't come to your games. Maybe if you put half the effort into the team
as you do in failing to run the companies your parents gave you, we'd actually have a winner. Enjoy the desert.
When you have hungover visiting fans puking around your shiny new stadium and no A's fans in sight, maybe you'll
remember this email. Or the one coming in 5 minutes.

Sincerely,

{sender_name}

Oakland A's fan"""

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
