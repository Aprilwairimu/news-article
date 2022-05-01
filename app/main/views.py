
from flask import render_template,request,redirect,url_for
from pip import main
from .import main
from ..requests import get_news,search_news,get_articles


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    general_news = get_news('general')
    business_news = get_news('business')
    political_news = get_news('political')

    title = 'Home - Welcome to The best news Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.index')('search',news_name=search_news))
    else:
        return render_template('index.html', general = general_news,business = business_news,politics = political_news )
    
@main.route('/news/<int:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_news(id)
    title = f'{news.title}'
    # reviews = Review.get_reviews(news.id)
    return render_template('movie.html',title = title,news = news)

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

# @main.route('/news/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     # form = ReviewForm()
#     news = get_news(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(news.id,title,news.poster,review)
#         new_review.save_review()
#         return redirect(url_for('main.new_review')('news',id = news.id ))

#     title = f'{news.title} review'
#     return render_template('new_review.html',title = title, review_form=form, news=news)







