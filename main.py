
import requests
import random
from twilio.rest import Client

# Set the stock and news companies and API keys
STOCK_COMPANY = "TSLA"
NEWS_COMPANY = "Tesla inc"
News_API = "YOUR_NEWS_API_KEY"
stock_api = "YOUR_ALPHAVANTAGE_API_KEY"

# Set the symbol to default to up arrow
symbol = "⬆️"

# Set the API endpoints for the stock and news APIs
Stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"

# Set the parameters for the stock API request
stock_parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_COMPANY,
    "outputsize":"compact",
    "apikey": stock_api
}

# Make the stock API request and get the list of dates
data=requests.get(url=Stock_endpoint,params=stock_parameters)
date_list=[key for key in data.json()["Time Series (Daily)"]]

# Get the close price from yesterday and the day before
yesterday_close=float(data.json()["Time Series (Daily)"][date_list[0]]["4. close"])
day_bfre_yesterday=float(data.json()["Time Series (Daily)"][date_list[1]]["4. close"])

# Calculate the difference between the two prices and update the symbol if it's down
different=str(yesterday_close-day_bfre_yesterday)
if "-" in different:
    symbol="⬇️"

# Calculate the percentage difference and send a news update if it's over 1%
different_percentage=abs((float(different)/yesterday_close)*100)
if different_percentage>=1:
    news_params={
        "q":NEWS_COMPANY,
        "apiKey":News_API,
        "searchIn":NEWS_COMPANY
    }

    # Make the news API request and get the top 3 articles
    newss = requests.get(news_endpoint, params=news_params)
    articles = newss.json()["articles"][:3]
    titles = [article["title"] for article in articles]
    descriptions = [article["description"] for article in articles]

    # Initialize the Twilio client with your account SID and auth token
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    # Send a message for each article
    for i in range(3):
        message = client.messages \
            .create(
            body=f"TSLA {symbol}\n {titles[i]}\n{descriptions[i]} ",
            from_='+YOUR_TWILIO_PHONE_NUMBER',
            to='+YOUR_PHONE_NUMBER'
        )

        print(message.sid)
