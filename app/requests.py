import urllib.request,json
from .models import Articles,Sources
import os
import requests
api_key = None
s_url = None
art_url = None
articles_url=None
def configure_request(app):
    global api_key,s_url,art_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    articles_url = app.config['SOURCE_ARTICLES_URL']
    s_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_APL_URL']

def get_sources(category):
    """
    function that gets response from the api call
    """
    sources_url = s_url.format(category,api_key)
    with urllib.request.urlopen(sources_url) as url:

        sources_data = url.read()
        response = json.loads(sources_data)        
        sources_outcome = None        
        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

def process_new_sources(sources_list):

    sources_outcome = []    
    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)    
    return sources_outcome

def get_articles(article):    
        articles_url = art_url.format(article,api_key)
    # print(art_url)
        with urllib.request.urlopen(articles_url) as url:
            articles_data = url.read()
            articles_response = json.loads(articles_data)        
            articles_outcome = None        
            if articles_response['articles']:
                articles_outcome_items = articles_response['articles']
                articles_outcome = process_new_articles(articles_outcome_items)
        return articles_outcome

def process_new_articles(articles_list):
    articles_outcome = []    
    for one_article in articles_list:
        source = one_article.get("source")
        author = one_article.get("author")
        description = one_article.get("description")
        title = one_article.get("title")
        url = one_article.get("url")
        urlToImage = one_article.get("urlToImage")
        publishedAt = one_article.get("publishedAt")
        new_article = Articles(source, author, title, description, url, urlToImage, publishedAt)
        articles_outcome.append(new_article)    
    return articles_outcome

def articles_source(source):
    sources_a_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source,api_key)    
    with urllib.request.urlopen(sources_a_url) as url:
        art_data = url.read()
        response = json.loads(art_data)
        source_articles = None        
        if response['articles']:
            source_articles_list = response['articles']
            source_articles = process_articles_source(source_articles_list)
    return source_articles

def process_articles_source(article_list):
    source_articles = []
    for art in article_list:
        source = art.get("source")
        author = art.get('author')
        title = art.get('title')
        description = art.get('description')
        url = art.get('url')
        urlToImage = art.get('urlToImage')
        publishedAt = art.get('publishedAt')        
        article_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        source_articles.append(article_object)
    return source_articles
def search_articles(article_name):
    search_url = art_url.format(article_name,api_key)    
    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)        
        search_outcome= None        
        if search_response['articles']:
            all_search_results = search_response['articles']
            search_outcome = search_articles(all_search_results)
    return search_outcome