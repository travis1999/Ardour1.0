import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(name, email, message):
    mess = MIMEMultipart()
    mess['From'] = 'Ardour email service'
    mess['To'] = 'oneyajanet96@gmail.com'
    mess['Subject'] = f'{name} through the Ardour website sent the following '

    message += f'\n You can contact {name} at {email}.'

    mess.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        text = mess.as_string()
        server.login("travor.biz@gmail.com", "ftcmnmqtuvvekccq")
        server.sendmail("travor.biz@gmail.com", 'oneyajanet96@gmail.com', text)


if __name__ == "__main__":
    send("travor", 'trevoroguna@gmail.com', 'This service sucks.')
