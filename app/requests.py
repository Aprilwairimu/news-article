# from app import app

import urllib.request,json
from app.models import Article,News
import os



# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']



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
            news_results = process_news_results(news_results_list)


    return news_results

def process_news_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        imageurl = news_item.get('imageurl')
        description = news_item.get('description')
        
       

        
        news_object = news_list(id,name,imageurl,description,)
        news_results.append(news_object)

    return news_results

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/{}?apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_news_results(search_news_list)


    return search_news_results

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



def process_article_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain news details

    Returns :
        article_results: A list of news objects
    '''
    article_results = []
    for article_item in article_list:
        name = article_item.get('name')
        title = article_item.get('title')
        description = article_item.get('description')
        
       

        
        article_object = article_list(id,name,description)
        article_results.append(article_object)

    return article_results

def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/{}?apiKey={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            all_search_results = search_article_response['results']
            search_article_results = process_article_results(all_search_results)


    return search_article_results






