import nntplib
from .base_source import NewsSource

class NNTPSource(NewsSource):
    def __init__(self, server, group):
        self.server = server
        self.group = group

    def fetch(self):
        news = []
        try:
            with nntplib.NNTP(self.server) as nntp:
                resp, count, first, last, name = nntp.group(self.group)
                last = int(last)
                first = max(int(first), last - 10)

                for i in range(last, first - 1, -1):
                    try:
                        resp, info = nntp.head(str(i))
                        lines = [line.decode() for line in info.lines]
                        title_line = next((line for line in lines if line.startswith('Subject:')), 'Subject: (No Title)')
                        title = title_line.replace('Subject: ', '').strip()
                        news.append({
                            'title': f"{title}",
                            'summary': "No summary available (NNTP article body skipped)",
                            'url': f"{self.server}/{self.group}/{i}",
                            'timestamp': ""
                        })
                    except Exception as e:
                        continue
        except Exception as e:
            print(f"Failed to fetch NNTP news: {e}")
        return news
