from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from . import models


@admin.register(models.Game)
class GameAdmin(OrderedModelAdmin):
    list_display = (str, 'move_up_down_links')


@admin.register(models.Phase)
class PhaseAdmin(OrderedModelAdmin):
    list_display = (str, 'move_up_down_links')
