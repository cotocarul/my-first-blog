from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Person(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	age = models.IntegerField(null=True, blank=True)



class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):# __unicode__ on Python 2
        return self.full_name
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):# __unicode__ on Python 2
        return self.headline