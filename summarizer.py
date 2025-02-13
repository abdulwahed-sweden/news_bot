# Summarizing News Using DeepSeek AI

import requests
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_BASE_URL

def summarize_news(news):
    """Summarize fetched news using DeepSeek AI."""
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    summarized_news = []
    
    for item in news:
        prompt = f"Summarize the following news in two sentences:\n\nTitle: {item['title']}\nSource: {item['source']}\nLink: {item['link']}"
        
        response = requests.post(
            f"{DEEPSEEK_API_BASE_URL}/v1/completions",
            headers=headers,
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
        )

        if response.status_code == 200:
            summary = response.json()["choices"][0]["message"]["content"]
        else:
            summary = "⚠️ AI failed to summarize this news."

        summarized_news.append({
            "source": item["source"],
            "title": item["title"],
            "summary": summary,
            "link": item["link"]
        })
    
    return summarized_news
