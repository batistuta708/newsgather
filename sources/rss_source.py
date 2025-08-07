import feedparser
from .base_source import NewsSource

class RSSSource(NewsSource):
    def __init__(self, url):
        self.url = url

    def fetch(self):
        feed = feedparser.parse(self.url)
        news = []
        for entry in feed.entries[:5]:  # Limit to top 5 entries
            news.append({
                'title': entry.title,
                'summary': entry.summary if 'summary' in entry else '',
                'url': entry.link,
                'timestamp': entry.published if 'published' in entry else ''
            })
        return news
