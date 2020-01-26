from django.contrib import admin

# Register your models here.

from .models import Genre, Game, Gamer, Publisher, Purchases

#admin.site.register(Game)
#admin.site.register(Gamer)
#admin.site.register(Purchases)
admin.site.register(Publisher)
admin.site.register(Genre)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'about')

@admin.register(Gamer)
class GamerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('gamer', 'game', 'date_purchased', 'price', 'review')
