# Stock Market Analysis and News Alert System

This is a Python script that fetches the stock market data of a specific company and sends an SMS message alert with the latest news about that company if the stock price increases or decreases by more than 1%.

## Dependencies

This project requires the following dependencies:

- requests
- twilio

You can install them using the following command:

```bash
pip install -r requirements.txt


# Usage
To use this script, you need to set the following environment variables:

NEWS_API_KEY: your News API key
ALPHAVANTAGE_API_KEY: your Alpha Vantage API key
TWILIO_ACCOUNT_SID: your Twilio account SID
TWILIO_AUTH_TOKEN: your Twilio auth token
FROM_NUMBER: your Twilio phone number
TO_NUMBER: the phone number where you want to receive the SMS alerts
You can set these variables by creating a .env file in the root directory of your project and adding them like this:

NEWS_API_KEY=your_news_api_key
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
FROM_NUMBER=your_twilio_phone_number
TO_NUMBER=your_phone_number

Then, run the script using the following command:

python stock_alert.py

The script fetches the stock market data for the TSLA company and sends an SMS alert if the stock price changes by more than 1%. You can modify the company and news sources by changing the STOCK_COMPANY and NEWS_COMPANY variables in the script.

