from django.contrib import admin
from post.models import *

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', )

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')

class Post_thanksAdmin(admin.ModelAdmin):
    list_display = ('contents', 'writer')

class Board_thanksAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Post_thanks, Post_thanksAdmin)
admin.site.register(Board_thanks, Board_thanksAdmin)

