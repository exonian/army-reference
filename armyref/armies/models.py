from django.db import models
from ordered_model.models import OrderedModel


class Game(OrderedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Phase(OrderedModel):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    order_with_respect_to = 'game'

    def __str__(self):
        return '{name} ({game})'.format(name=self.name, game=self.game)
