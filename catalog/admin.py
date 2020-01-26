from django.contrib import admin

# Register your models here.

from .models import Genre, Game, Gamer, Publisher, Purchases

admin.site.register(Game)
admin.site.register(Gamer)
admin.site.register(Purchases)
admin.site.register(Publisher)
admin.site.register(Genre)
