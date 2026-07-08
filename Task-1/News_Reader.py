import requests
news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=e36536bdfe1b44a6ba61a8af6f7c8a9d"
# e36536bdfe1b44a6ba61a8af6f7c8a9d api key
def News_Reading():
    news_response = requests.get(news_url)
    news_data = news_response.json()
    articles_list = news_data["articles"]
    display_articles =""
    if news_data["totalResults"] == 0:
        return "I'm sorry, I couldn't find any news headlines right now."
    
        
    for single_articles in articles_list[:2] :
        headline = single_articles["title"]
        display_articles += headline + "\n"
    return display_articles
        
News_Reading()