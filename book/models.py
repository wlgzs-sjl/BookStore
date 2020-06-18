from django.db import models


# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=32, unique=True)
    book_author = models.CharField(max_length=32,)
    book_type = models.CharField(max_length=32,)
    book_price = models.CharField(max_length=32,)
    book_press = models.CharField(max_length=32,)

