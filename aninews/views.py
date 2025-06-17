from django.shortcuts import render
import requests
import feedparser
import time
import random
from datetime import datetime

def home(request, anime_id=None):
    news_type = ""
    news = []
    error_message = None
    last_request_time = request.session.get('last_news_request', 0)
    current_time = time.time()

    if request.method == "POST":
        news_type = request.POST.get("type", "").lower().strip()

        # Rate limiting
        if current_time - last_request_time < 1.0:
            time.sleep(1.0 - (current_time - last_request_time))

        # Try multiple RSS feeds for anime news
        rss_feeds = [
            "https://www.animenewsnetwork.com/all/rss.xml",  # ANN RSS feed
            "https://myanimelist.net/rss/news.xml",          # MAL news (if available)
        ]
        
        news_items = []
        
        for feed_url in rss_feeds:
            try:
                request.session['last_news_request'] = time.time()
                
                # Use feedparser for RSS feeds
                feed = feedparser.parse(feed_url)
                
                for entry in feed.entries[:10]:  # Get up to 10 items per feed
                    # Parse publication date
                    pub_date = ""
                    if hasattr(entry, 'published'):
                        try:
                            pub_date = entry.published
                        except:
                            pub_date = "Unknown"
                    
                    # Get description/summary
                    description = ""
                    if hasattr(entry, 'summary'):
                        description = entry.summary
                    elif hasattr(entry, 'description'):
                        description = entry.description
                    
                    news_items.append({
                        "title": entry.title if hasattr(entry, 'title') else "",
                        "description": description,
                        "link": entry.link if hasattr(entry, 'link') else "",
                        "pub_date": pub_date
                    })
                
                break  # If successful, don't try other feeds
                
            except Exception as e:
                continue  # Try next feed if this one fails

        if not news_items:
            # Fallback: Create sample news items for demonstration
            news_items = [
                {
                    "title": "Sample Anime News 1",
                    "description": "Sorry. We are on maintaneance or having some internal problems.",
                    "link": "https://www.animenewsnetwork.com",
                    "pub_date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
                },
                {
                    "title": "Sample Anime News 2", 
                    "description": "Sorry. We are on maintaneance or having some internal problems.",
                    "link": "https://www.animenewsnetwork.com",
                    "pub_date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
                }
            ]

        if news_type:
            # Filter news by title or description
            news = [
                item for item in news_items
                if news_type in item["title"].lower() or
                   news_type in item["description"].lower()
            ]
        else:
            # Randomly select up to 5 recent news items
            random.shuffle(news_items)
            news = news_items[:10]

        if not news and news_type:
            error_message = f"No news found for type '{news_type}'."
            
    else:
        # On GET, try to fetch news
        if current_time - last_request_time < 1.0:
            time.sleep(1.0 - (current_time - last_request_time))
            
        try:
            request.session['last_news_request'] = time.time()
            
            # Try ANN RSS feed
            feed = feedparser.parse("https://www.animenewsnetwork.com/all/rss.xml")
            news_items = []
            
            for entry in feed.entries[:10]:
                pub_date = ""
                if hasattr(entry, 'published'):
                    pub_date = entry.published
                
                description = ""
                if hasattr(entry, 'summary'):
                    description = entry.summary
                elif hasattr(entry, 'description'):
                    description = entry.description
                
                news_items.append({
                    "title": entry.title if hasattr(entry, 'title') else "",
                    "description": description,
                    "link": entry.link if hasattr(entry, 'link') else "",
                    "pub_date": pub_date
                })
            
            random.shuffle(news_items)
            news = news_items[:10]
            
        except Exception as e:
            error_message = f"Error fetching news: {str(e)}"
            # Fallback sample data
            news = [
                {
                    "title": "News Unavailable",
                    "description": "Unable to fetch live news. The API endpoint may be unavailable.",
                    "link": "https://www.animenewsnetwork.com",
                    "pub_date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
                }
            ]

    return render(request, "anime_news.html", {
        "news": news,
        "selected_type": news_type,
        "error_message": error_message,
    })