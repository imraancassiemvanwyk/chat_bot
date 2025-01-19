import requests

def get_news():
    api_key = "your key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        news = "\n".join([f"- {article['title']}" for article in articles[:5]])
        return f"Here are today's top news headlines:\n{news}"
    else:
        return "I couldn't fetch the news right now. Please try again later."