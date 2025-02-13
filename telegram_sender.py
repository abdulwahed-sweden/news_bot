# Sending News to Telegram Channel

from telegram import Bot
import time
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

def send_news_to_telegram(summarized_news):
    """Send summarized news to a Telegram channel."""
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    for news in summarized_news:
        message = f"""
📰 **Source:** {news['source']}
📌 **Title:** {news['title']}
📝 **Summary:** {news['summary']}
🔗 [Read More]({news['link']})
        """
        
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message, parse_mode="Markdown")
        time.sleep(3)  # Prevent spam
