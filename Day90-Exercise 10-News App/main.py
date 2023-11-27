#use newsapi and the request module to fetch the daily news related to different topics.
import requests
import json
query=input("What type of news?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-10-25&sortBy=publishedAt&apiKey=b7b382c2f5184b1fbd72d071a77562c6"
r=requests.get(url)
news=json.loads(r.text)
for r in news["articles"]:
    print(r["title"])
    print(r["description"])
    print("-----------------")
