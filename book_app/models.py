from django.db import models


# Create your models here.
from book_app.validators import clean_pages


class Book(models.Model):
    title = models.CharField(max_length=50)
    pages = models.IntegerField(default=0,)
    description = models.TextField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'Title: {self.title}, Pages: {self.pages}, Description: {self.description}, Author: {self.author}'
