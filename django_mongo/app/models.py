from djongo import models

class Post(models.Model):
    title_news = models.CharField(max_length=100)
    category = models.TextField()
    data = models.CharField(max_length=100)
    url_img = models.CharField(max_length=100)

    def __str__(self):
        return self.title
