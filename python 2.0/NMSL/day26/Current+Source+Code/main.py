import requests
import smtplib, ssl
from send_email import email

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# for article in content["articles"]:
#     print(article["title"])
#     print(article["description"])

OverallNews = []
# Access the article titles and description
for article in content["articles"]:
      news = article["title"] + "\n" + str(article["description"]) + "\n\n"
      OverallNews.append(news)

raw_msg = "".join(OverallNews)

message = f"""\
Subject: DAY26 news
{raw_msg}
"""

email(message.encode("utf8"))
print("success!")