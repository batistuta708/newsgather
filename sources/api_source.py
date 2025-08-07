import requests
from .base_source import NewsSource
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class APINewsSource(NewsSource):
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.url = "https://newsapi.org/v2/top-headlines?country=us"

    def get_news(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(self.url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            return [f"{a['title']} - {a.get('description', '')}" for a in articles]
        else:
            return [f"Error fetching news: {response.status_code} - {response.text}"]
