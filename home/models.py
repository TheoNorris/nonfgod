from django.db import models


class Artwork(models.Model):
    name = models.CharField(max_length=100)
    collection_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
