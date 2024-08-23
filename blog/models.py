from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from tinymce.models import HTMLField

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = CKEditor5Field(config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='blog_posts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    allow_comments = models.BooleanField(default=True)
    
    def publish(self):
        self.published_at = timezone.now()
        self.is_published = True
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'