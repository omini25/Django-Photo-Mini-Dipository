from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, )
    added = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    added = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.description
