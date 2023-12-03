import requests
import json

query=input("What type of news are you interested in ?")

url="https://newsapi.org/v2/everything?q={query}&from=2023-10-27&sortBy=publishedAt&apiKey=b7b382c2f5184b1fbd72d071a77562c6"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  