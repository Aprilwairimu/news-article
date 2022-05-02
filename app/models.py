class Articles:
    '''
    Article class to define Class Objects
    '''  
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):        
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt
        
class ArticleReview:    
    articles_reviews = []   

    def __init__(self,title,urlToImage,review):
        self.title = title
        self.urlToImage = urlToImage
        self.review = review 

    def save_artcles_review(self):
        ArticleReview.articles_reviews.append(self) 

@classmethod
def clear_articles_reviews(cls):
    ArticleReview.articles_reviews.clear() 

@classmethod
def get_articles_reviews(cls,title):        
    article_results = []        
    for review in cls.articles_reviews:
        if review.title== title:
            article_results.append(review)        
    return article_results

class Sources:
    '''
    News class to define News Objects
    ''' 
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class SourcesReview:    
    source_reviews = []    
    def __init__(self,id,title,url,review):
        self.id = id
        self.title = title
        self.url = url
        self.review = review 

    def save_sources_review(self):
        SourcesReview.source_reviews.append(self)  

@classmethod
def clear_source_reviews(cls):
    SourcesReview.source_reviews.clear() 

@classmethod
def get_source_reviews(cls,id):        
        source_results = []        
        for review in cls.source_reviews:
            if review.id == id:
                source_results.append(review)        
        return source_results