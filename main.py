import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(receiver_email , text):

    sender_email = "bobirjonmuxammadov20314@gmail.com"
    password = "davmilkynsicldlz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    # context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
send_mail("bobirjonmuxammadov20314@gmail.com","Hello,world")