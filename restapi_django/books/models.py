from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=99)
    description = models.TextField()
    published = models.DateField()

    def __str__(self):
        return self.title
