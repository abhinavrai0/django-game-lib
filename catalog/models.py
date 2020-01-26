from django.db import models
import uuid

# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Publisher(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):

    title = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL,  null=True)
    about = models.CharField(max_length=1000)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Gamer(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    games = models.ManyToManyField(Game, through='Purchases')

    def __str__(self):
        return self.name


class Purchases(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_purchased = models.DateField()
    price = models.IntegerField()
    review = models.CharField(max_length=1000)

    def __str__(self):
        return self.game.title
