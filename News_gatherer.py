import argparse
from sources.rss_source import RSSSource
from sources.nntp_source import NNTPSource
from sources.api_source import NewsSource as APINewsSource
from dispatch.file_dispatch import FileDispatcher
from dispatch.email_dispatch import EmailDispatcher
from reports.report_generator import generate_report

# 1. Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("--source", choices=["rss", "api", "nntp"], required=True)
parser.add_argument("--destination", choices=["file", "email", "pdf"], required=True)
parser.add_argument("--interval", type=int, help="Run every N minutes (optional)")
args = parser.parse_args()

# 2. Select News Source

if args.source == 'rss':
    from sources.rss_source import RSSSource
    source = RSSSource()
elif args.source == 'api':
    from sources.api_source import APINewsSource
    source = APINewsSource()
elif args.source == 'nntp':
    from sources.nntp_source import NNTPSource
    source = NNTPSource()
else:
    raise ValueError(f"Unknown source: {args.source}")


# 3. Get Content
content = source.get_news()

# 4. Dispatch/Output
if args.destination == "file":
    dispatcher = FileDispatcher()
    dispatcher.dispatch(content)

elif args.destination == "email":
    dispatcher = EmailDispatcher(
        sender_email="youremail@example.com",
        sender_password="your-app-password",
        recipient_email="recipient@example.com"
    )
    dispatcher.dispatch(content)

elif args.destination == "pdf":
    generate_report(content)

else:
    print("[x] Invalid destination.")

NEWS_API_KEY="your_actual_api_key_here"
