import os
class Config:    
    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}' 

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass
class DevConfig(Config):

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}