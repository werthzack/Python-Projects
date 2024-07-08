from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

website = BeautifulSoup(response.text, "html.parser")
articles = website.find_all(name="span", class_="titleline")
article_links = [tag.find(name="a").get("href") for tag in articles]
article_texts = [tag.find(name="a").string for tag in articles]
article_votes = [int(score.string.strip(" points")) for score in website.find_all(class_="score")]

top_index = article_votes.index(max(article_votes))
print(article_texts[top_index])
print(article_links[top_index])
print(max(article_votes))
