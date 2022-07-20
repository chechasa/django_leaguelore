from django.contrib import admin
from .models import Tag, Champion, Stats, Abilities
# Register your models here.
admin.site.register(Tag)
admin.site.register(Champion)
admin.site.register(Stats)
admin.site.register(Abilities)