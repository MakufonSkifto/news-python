import news_python

news = news_python.Country(key="API-KEY")
news_content = news.get_news(country="us", category="tech")

print(f"Title: {news_content.title}\n"
      f"URL: {news_content.url}\n"
      f"Author: {news_content.author}")
