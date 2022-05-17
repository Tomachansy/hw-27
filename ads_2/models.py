from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
