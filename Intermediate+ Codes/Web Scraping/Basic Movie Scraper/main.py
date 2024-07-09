import requests
from bs4 import BeautifulSoup
import html

response = requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
response.encoding = 'utf-8'
website = BeautifulSoup(response.text, "html.parser")
articles = website.find_all(class_="article-title-description")

with open("movies.txt", "w", encoding='utf-8') as file:
    for i in range(len(articles)-1, -1, -1):
        article = articles[i]
        title = article.find(class_="title").string
        print(html.unescape(title))
        file.write(title + "\n")