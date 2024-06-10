from django.contrib import admin
from .models import Player, GameScore


admin.site.register([Player, GameScore])
