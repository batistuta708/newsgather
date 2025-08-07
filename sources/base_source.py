from abc import ABC, abstractmethod

class NewsSource(ABC):
    @abstractmethod
    def fetch(self):
        """
        Fetch news articles and return a list of dictionaries.
        Each dictionary should include: title, summary, url, timestamp.
        """
        pass
