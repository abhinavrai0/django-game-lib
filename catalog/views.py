from django.shortcuts import render
from catalog.models import Game, Gamer, Publisher, Purchases, Genre

# Create your views here.


def index(request):
    num_games = Game.objects.all().count()
    num_purchases = Purchases.objects.all().count()
    num_publishers = Publisher.objects.all().count()
    num_gamers = Gamer.objects().all().count()
    context = {
        'num_games':  num_games,
        'num_purchases': num_purchases,
        'num_publishers': num_publishers,
        'num_gamers': num_gamers,
    }
    return render(request, 'index.html', context=context)

