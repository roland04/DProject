from django.contrib import admin

from .models import Planet, Location, Resource, Item

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'locationtype', 'planet')

admin.site.register(Planet, PlanetAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Resource)
admin.site.register(Item)
