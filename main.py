# Executing the Bot and Scheduling the Bot to Run

import schedule
import time
from news_fetcher import fetch_news
from summarizer import summarize_news
from telegram_sender import send_news_to_telegram

def run_news_bot():
    """Main function to fetch, summarize, and send news to Telegram."""
    print("🔄 Fetching latest news...")
    news_list = fetch_news()
    
    if news_list:
        summarized_news = summarize_news(news_list)
        send_news_to_telegram(summarized_news)
        print("✅ News successfully sent to Telegram channel")
    else:
        print("⚠️ No new news updates available.")

# Schedule the bot to run every 30 minutes
schedule.every(30).minutes.do(run_news_bot)

print("🚀 News bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
