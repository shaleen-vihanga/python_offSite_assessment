import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(past_price,present_price, price_difference):
    sender_email = "shaleenvihanga@gmail.com"
    recipient_email = "vihangashaleen@gmail.com"
    subject = "Apple Stock Price Alert"

    body = f"The stock price of Apple Inc. (AAPL) has changed.\n\nPast Value: ${past_price}\nPresent Value: ${present_price}\nValue Difference : ${price_difference}\n\nPlease note the change in stock price and take necessary action."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, "mkah jsbd gegf nhoi")
    text = msg.as_string()
    server.sendmail(sender_email,recipient_email, text)
    server.quit()
