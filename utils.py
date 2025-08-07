import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='news_gather.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
