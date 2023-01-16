from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    github_link = models.CharField(max_length=500)
    tech_stack = models.TextField()
    #image = models.FilePathField(path="/img")
