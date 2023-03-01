# Stock Market News Alert

This is a Python script that tracks daily stock data of a company and sends SMS alerts to users about the change in stock price along with relevant news articles. It uses the Alpha Vantage API to fetch the daily stock data and the News API to fetch news articles related to the company. The Twilio API is used to send the SMS alerts to users.

## Installation
1. Clone the repository to your local machine:
 ```
 git clone https://github.com/{username}/{repository-name}.git
```
2. Change directory to the project directory:
```
cd {repository-name}
```
3. Install the required packages:
```
pip install -r requirements.txt
```
# Usage
1.Open the **'main.py'** file in a code editor.

2.Set the value of **'STOCK_COMPANY'** and **'NEWS_COMPANY'** variables to the stock company and its name respectively.

3.Create accounts and obtain API keys for the Alpha Vantage, News API, and Twilio services.

4.Set the values of stock_api, News_API, account_sid, and auth_token variables to the API keys and account details obtained in the previous step.

5.Set the values of from_ and to variables to the phone numbers in the international format.

6.Run the script using the following command:
```
python main.py

```
## Contributing
contributions are welcome! Please feel free to submit a pull request or create a issue if you have any sugggestions or find any bugs.




