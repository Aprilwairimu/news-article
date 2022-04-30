class Article:
    """Article class to define Article objects
    """
    def __init__(self,Author,title,description,url,urlToImage,publishedAt):
        self.Author =id
        self.title = title
        self.description = description
        self.url = urlToImage
        self.urlToImage = "https://image.tmdb.org/t/p/w500/" + poster
        self.publishedAt = publishedAt



class ArticleReview:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
