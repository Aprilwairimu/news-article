from re import U
from unittest import result
from urllib import response


class News:
    '''
     News class to define Movie Objects
    '''

    def __init__(self,news_id,name,description,url,vote):
        self.id =news_id
        self.name = name
        self.description = description
        self.url= url 
        



class NewsReview:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.movie_id = news_id
        self.title = title
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
