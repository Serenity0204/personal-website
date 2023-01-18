from django.db import models

# Create your models here.



class PublishedProjectManager(models.Manager):  
    def get_queryset(self):
        return super(PublishedProjectManager, self).get_queryset().filter(status='published')


class Project(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=100)
    detail = models.TextField()
    github_link = models.CharField(max_length=500)
    tech_stack = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    #image = models.FilePathField(path="/img")
    def __str__(self):
        return self.name
    
