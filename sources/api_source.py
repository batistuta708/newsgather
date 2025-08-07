import os
import requests
from sources.base_source import NewsSource  # adjust if your base class is elsewhere

class APINewsSource(NewsSource):
    def __init__(self):
        self.api_key = os.getenv("NEWSAPI_KEY")
        self.url = "https://newsapi.org/v2/top-headlines?country=us"


    def get_news(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [
                {
                    "title": article.get("title"),
                    "description": article.get("description"),
                    "url": article.get("url")
                }
                for article in articles
            ]
        else:
            raise Exception(f"API request failed: {response.status_code} {response.text}")

    def fetch(self):
        return self.get_news()