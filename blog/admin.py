from django.contrib import admin
from .models import BlogPost, Subject

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'author', 'subjects')
    search_fields = ('title', 'content', 'tags')
    date_hierarchy = 'created_at'
    filter_horizontal = ('subjects',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'tags', 'is_published', 'allow_comments')
        }),
        ('Dates', {
            'fields': ('created_at', 'published_at'),
            'classes': ('collapse',),
        }),
        ('Additional Information', {
            'fields': ('thumbnail', 'meta_description', 'title_2', 'title_3', 'title_4', 'title_5', 'title_6', 
                       'text_1', 'text_2', 'text_3', 'text_4', 'text_5', 'text_6', 'text_7', 'text_8', 'text_9', 'text_10',
                       'picture_1', 'picture_2', 'picture_3', 'picture_4', 'picture_5', 'picture_6', 'picture_7', 'picture_8', 'picture_9', 'picture_10'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
