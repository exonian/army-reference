from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from . import models


@admin.register(models.Reference)
class ReferenceAdmin(OrderedModelAdmin):
    list_display = (str, 'move_up_down_links')
