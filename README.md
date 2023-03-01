# Stock-Market-News-Alert
Stock Market News Alert
This is a Python script that uses the Alpha Vantage and News API to fetch the daily stock data for Tesla and sends an SMS alert if the stock price goes up or down by more than 1%.

Prerequisites
To run this script, you need to have the following:

Python 3 installed on your machine
requests and twilio Python packages installed
An Alpha Vantage API key for accessing stock data
A News API key for accessing news data
A Twilio account for sending SMS alerts
Installation
Clone this repository to your local machine

Install the required Python packages by running pip install -r requirements.txt

Set the environment variables for Alpha Vantage API key, News API key, Twilio Account SID, Twilio Auth Token, and Twilio phone numbers to send SMS alerts to. You can either set them as system environment variables or create a .env file in the root directory of the project and add them there.

bash
Copy code
ALPHAVANTAGE_API_KEY=<your_alpha_vantage_api_key>
NEWS_API_KEY=<your_news_api_key>
TWILIO_ACCOUNT_SID=<your_twilio_account_sid>
TWILIO_AUTH_TOKEN=<your_twilio_auth_token>
FROM_NUMBER=<your_twilio_phone_number>
TO_NUMBER=<the_phone_number_to_receive_sms_alerts>
Run the script using python stock_alert.py

Usage
When you run the script, it fetches the daily stock data for Tesla from the Alpha Vantage API and calculates the percentage change in the stock price from the previous day. If the percentage change is more than 1%, it fetches the latest news articles related to Tesla from the News API and sends an SMS alert using the Twilio API with the top 3 news article titles and descriptions.
