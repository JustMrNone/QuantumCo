from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
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
    
    # New optional title fields
    title_2 = models.CharField(max_length=200, blank=True, null=True)
    title_3 = models.CharField(max_length=200, blank=True, null=True)
    title_4 = models.CharField(max_length=200, blank=True, null=True)
    title_5 = models.CharField(max_length=200, blank=True, null=True)
    title_6 = models.CharField(max_length=200, blank=True, null=True)
    
    # New optional text fields
    text_1 = models.TextField(blank=True, null=True)
    text_2 = models.TextField(blank=True, null=True)
    text_3 = models.TextField(blank=True, null=True)
    text_4 = models.TextField(blank=True, null=True)
    text_5 = models.TextField(blank=True, null=True)
    text_6 = models.TextField(blank=True, null=True)
    text_7 = models.TextField(blank=True, null=True)
    text_8 = models.TextField(blank=True, null=True)
    text_9 = models.TextField(blank=True, null=True)
    text_10 = models.TextField(blank=True, null=True)

    # New optional picture fields
    picture_1 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_2 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_3 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_4 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_5 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_6 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_7 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_8 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_9 = models.ImageField(upload_to='pictures/', blank=True, null=True)
    picture_10 = models.ImageField(upload_to='pictures/', blank=True, null=True)

#well, this ain't efficient at all! probably will create custum page for this 

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