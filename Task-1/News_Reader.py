import requests
news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=e36536bdfe1b44a6ba61a8af6f7c8a9d"
# e36536bdfe1b44a6ba61a8af6f7c8a9d api key
def News_Reading():
    news_response = requests.get(news_url)
    news_data = news_response.json()
    print(news_data)
    articles_list = news_data["articles"]

    if news_data["totalResults"] == 0:
        return "I'm sorry, I couldn't find any news headlines right now."
    
    else :
        for single_articles in articles_list :
            headline = single_articles["title"]
            return headline
    

News_Reading()