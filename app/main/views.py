
from flask import render_template,request,redirect,url_for
from pip import main
from .import main
from ..requests import get_sources,get_articles,search_articles,articles_source


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    general_news = get_sources('general')
    business_news = get_sources('business')
    political_news = get_sources('political')

    return render_template('index.html', general = general_news,business = business_news,politics = political_news )
    
# @main.route('/news/<int:id>')
# def news(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     movie = get_sources(id)
#     title = f'{news.title}'
#     # reviews = Review.get_reviews(news.id)
#     return render_template('movie.html',title = title,news = news)

# @main.route('/search/<news_name>')
# def search(news_name):
#     '''
#     View function to display the search results
#     '''
#     news_name_list = news_name.split(" ")
#     news_name_format = "+".join(news_name_list)
#     searched_news = search_news(news_name_format)
#     title = f'search results for {news_name}'
#     return render_template('search.html',news = searched_news)








