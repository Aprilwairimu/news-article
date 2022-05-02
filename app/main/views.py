from flask import render_template,redirect,request,url_for
from . import main
# from app import app
from ..requests import get_sources,get_articles,search_articles,articles_source

@main.route('/')
def HomePage():
    """
    Views thats renders news sources to the home page
    """
    general_news = get_sources("general")
    business_news = get_sources("business")
    sports_news = get_sources("sports")

    return render_template('index.html',general=general_news,business=business_news,sports=sports_news )

@main.route('/articles/<id>')
def sourceArticles(id):
    all_articles = articles_source(id)
    print(all_articles)
    source = id

    return render_template('sourcearticles.html', articles = all_articles, source = source)

@main.route('/News-Articles')
def NewsArticles():
    """
    View that would return news articles    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')

    return render_template('articles.html',health=health_articles, tech =education_articles)

@main.route('/search/<article_name>')
def articleSearch(article_name):
    """
    function that returns the searched articles
    """
    search_article_name = article_name.split("")
    search_name_format = "+".join(search_article_name)
    searched_articles = search_articles(search_name_format) 

    return render_template('search.html',articles = searched_articles)