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


class Warscroll(OrderedModel):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    order_with_respect_to = 'game'

    def __str__(self):
        return self.name


class Rule(OrderedModel):
    name = models.CharField(max_length=255)
    wording = models.TextField(blank=True)
    warscroll = models.ForeignKey(Warscroll, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class WeaponProfile(OrderedModel):
    MELEE = 'MELEE'
    MISSILE = 'MISSILE'
    TYPES = (
        (MELEE, 'Melee'),
        (MISSILE, 'Missile'),
    )

    name = models.CharField(max_length=255)
    weapon_type = models.CharField(max_length=15, choices=TYPES)
    wording = models.TextField(blank=True)
    warscroll = models.ForeignKey(Warscroll, on_delete=models.CASCADE)

    order_with_respect_to = 'warscroll'

    def __str__(self):
        return self.name
