import datetime as dt
import smtplib
import random


# Get the day of the week
now = dt.datetime.now()
week_day = now.weekday()

MY_MAIL = "fake_mail@gmail.com"
PASSWORD = "fake_password"

# Send mail when is Monday
if week_day == 0:

    # Get data from quotes.txt & Peek quote
    with open("quotes.txt") as file:
        motivational_quotes = [quote.strip() for quote in file.readlines()]

    quote_of_the_week = random.choice(motivational_quotes)

    # smtp.live.com -> hotmail
    # smtp.gmail.com -> gmail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Encrypt mail
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg=f"Subject:Quote of The Week\n\n{quote_of_the_week}")

