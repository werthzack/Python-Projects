import os
import requests
import datetime
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()


def post_news(text, date):
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": date,
        "sortBy": "popularity",
        "apiKey": os.getenv('NEWS_API')
    }
    news_url = 'https://newsapi.org/v2/everything'
    news_response = requests.get(news_url, news_parameters)
    news_data = news_response.json()['articles'][0]
    client = Client(os.getenv('SID'), os.getenv('AUTH_TOKEN'))
    message = client.messages \
        .create(
        body=f"""
    {text}
Update for {datetime.date.today()}
Headline: {news_data['title']}\n
Brief: {news_data['description']}\n
Link: {news_data['url']}
    """,
        from_="whatsapp:+14155238886",
        to="whatsapp:+2349124306538"
    )
    print(message.status)


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv('STOCK_API')
}

stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
stock_response = requests.get(stock_url)
data: dict = stock_response.json()['Time Series (Daily)']
for key, value in data.items():
    open_price = float(value['1. open'])
    close_price = float(value['4. close'])
    percentage = round((close_price - open_price) / close_price, 2)
    status_text = ""
    if percentage > 0.0:
        status_text = f"🔺 {percentage}%"
        post_news(status_text, key)
        break
    elif percentage < 0.0:
        status_text = f"🔻 {abs(percentage)}%"
        post_news(status_text, key)
        break
