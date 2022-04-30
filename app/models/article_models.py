class Article:
    """Article class to define Article objects
    """
    def __init__(self,Author,title,description,url,urlToImage,publishedAt):
        self.Author =id
        self.title = title
        self.description = description
        self.url = urlToImage
        self.urlToImage = "https://image.tmdb.org/t/p/w500/" 
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
