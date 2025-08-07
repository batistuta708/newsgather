from .base_dispatch import NewsDispatcher

class FileDispatcher(NewsDispatcher):
    def __init__(self, file_path):
        self.file_path = file_path

    def dispatch(self, report):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to {self.file_path}")
        except Exception as e:
            print(f"Failed to write file: {e}")
