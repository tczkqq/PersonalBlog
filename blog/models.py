from django.db import models
from django.utils import timezone
from django.shortcuts import reverse 
from django.db.models import Count
from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   
        
    
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    text = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    tags = models.ManyToManyField(Tag)

    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return f'{self.title} last updated at {self.updated}'

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[
            self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug
        ])



