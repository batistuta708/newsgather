from abc import ABC, abstractmethod

class NewsDispatcher(ABC):
    @abstractmethod
    def dispatch(self, report):
        """
        Send or save the compiled news report.
        """
        pass
