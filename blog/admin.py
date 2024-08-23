from django.contrib import admin
from .models import BlogPost, Subject

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'author', 'subjects')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    filter_horizontal = ('subjects',)  # Make selecting subjects easier

    class Media:
        js = [
            # Ensure this is the correct path or URL for CKEditor 5
            'https://cdn.ckeditor.com/ckeditor5/ckeditor.js',
        ]
        css = {
            'all': ('//cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css',)
        }

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)