from django.db import models
from django.utils import timezone

# Create your models here.



class PublishedProjectManager(models.Manager):  
    def get_queryset(self):
        return super(PublishedProjectManager, self).get_queryset().filter(status='published')


class Project(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # manager
    objects = models.Manager()
    published = PublishedProjectManager()


    # attributes
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    detail = models.TextField()
    github_link = models.CharField(max_length=500)
    tech_stack = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')    
    
    # date
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    #image = models.FilePathField(path="/img")
    def __str__(self):
        return self.name
    
