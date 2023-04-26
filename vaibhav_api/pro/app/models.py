from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='movies',default=1)


