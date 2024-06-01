from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')







admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)