from django.contrib import admin
from .models import Genre, Movies
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'numbers_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)