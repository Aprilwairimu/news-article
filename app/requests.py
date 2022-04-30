from app import app
# import urllib.request,json
# from .models import movie
import urllib.request,json
from .models import article_models,news_models


# Getting api key
api_key = None
# Getting the movie base url
base_url = None
art_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    # Article_url = app.config['']




# # Getting api key
# api_key = app.config['MOVIE_API_KEY']

# # Getting the movie base url
# base_url = app.config["MOVIE_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        poster = news_item.get('poster_path')
       

        if poster:
            news_object = news_models(id,name,description,poster,)
            news_results.append(news_object)

    return news_results

def get_articles(id):
    get_articles_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        news_object = None
        if articles_details_response:
            id = articles_details_response.get('id')
            title = articles_details_response.get('original_title')
            imageurl = articles_details_response.get('imageurl')
            review = articles_details_response.get('review')

            news_object = articles_details_response(id,title,imageurl,review)

    return news_object

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/{}?apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results




