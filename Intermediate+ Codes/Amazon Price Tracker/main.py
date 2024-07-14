import os

import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def main():
    practice_url = "https://appbrewery.github.io/instant_pot/"
    live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
    live_url2 = "https://www.amazon.com/Roku-Streaming-Device-Vision-Controls/dp/B09BKCDXZC?ref=dlx_deals_dg_dcl_B09BKCDXZC_dt_sl14_1f"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
    }
    response = requests.get(url=live_url2, headers=header)
    response.encoding = 'utf-8'
    web_html = BeautifulSoup(response.text, "html.parser")
    price_div = web_html.find(name="div", id="corePriceDisplay_desktop_feature_div")
    price_whole = price_div.find(name="span", class_="a-price-whole").getText().strip()
    price_fraction = price_div.find(name="span", class_="a-price-fraction").getText().strip()
    price_str = f"{price_whole}{price_fraction}"
    price = float(price_str)

    product_name = web_html.find(name="span", id="productTitle").getText()
    cleaned_text = ' '.join(product_name.split())
    if price < 100:
        send_mail(cleaned_text, price)


def send_mail(product: str, price: float):
    mail = input("Enter your mail: ")
    app_password = input("Enter you app password: ")
    target_mail = input("Enter the target mail: ")
    if app_password == "":
        print("Getting environment password...")
        app_password = os.getenv('email_app_password')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=mail, password=app_password)
        connection.sendmail(
            from_addr=f"Price Notifier <{mail}>",
            to_addrs=target_mail,
            msg=f"Subject: Cheap Price Alert!!!\n\n"
                f"Low price alert! Only ${price} to buy product {product}".encode('utf-8')
        )


if __name__ == '__main__':
    load_dotenv()
    main()
