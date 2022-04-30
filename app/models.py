class Article:
    """Article class to define Article objects
    """
    def __init__(self,source,Author,title,description,url,urlToImage,publishedAt):
        self.source =source
        self.Author = Author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage 
        self.publishedAt = publishedAt



class ArticleReview:

    all_reviews = []

    def __init__(self,title,imageurl,review):
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        ArticleReview.articles_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        ArticleReview.articles_reviews.clear()

    @classmethod
    def get_reviews(cls,title):

        article_response = []

        for review in cls.articles_reviews:
            if review.title == title:
                article_response.append(review)

        return article_response




from re import U
from unittest import result
from urllib import response


class News:
    '''
     News class to define Movie Objects
    '''

    def __init__(self,news_id,name,description,url,):
        self.id =news_id
        self.name = name
        self.description = description
        self.url= url 
        



class NewsReview:

    all_reviews = []

    def __init__(self,news_id,name,imageurl,review):
        self.movie_id = news_id
        self.name = name
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        NewsReview.news_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
       NewsReview.news_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        news_response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                news_response.append(review)

        return news_response






# import unittest
# from app.main.views import news
# from app.models import article_models
# from app.models import news_models
# News = news.News

# class NewsTest(unittest.TestCase):
#     '''
#     Test Class to test the behaviour of the News class
#     '''

#     def setUp(self):
#         '''
#         Set up method that will run before every Test
#         '''
#         self.new_news = news_models(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_news,news_models))


# class ArticalTest(unittest.TestCase):
#     '''
#     Test Class to test the behaviour of the News class
#     '''

#     def setUp(self):
#         '''
#         Set up method that will run before every Test
#         '''
#         self.new_Article = article_models(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_Article,article_models.Article))


# if __name__ == '__main__':
#     unittest.main()
