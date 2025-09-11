import datetime as dt
import smtplib
import random

def get_day_of_week():
    now = dt.datetime.now()
    return now.weekday()

def get_quotes():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        return [quote.strip() for quote in quotes]
    
def send_email(quote):
    my_email = ""
    my_password = ""
    to_email = ""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Today's quote\n\n{quote}")
        print(f"Sent quote:\n {quote}")

      
random_quote = random.choice(get_quotes())
today = get_day_of_week()
if today != 3:
    print("Today is not the day for an email!")
else:
    send_email(random_quote)