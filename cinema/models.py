from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    #wiki_link = models.URLField(blank=True, null=True)  # new field
   
    def __str__(self):
        return self.name
