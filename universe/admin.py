from django.contrib import admin

from .models import Planet, Location, Resource, Item, ItemResource

class ItemResourceInline(admin.TabularInline):
    model = ItemResource
    extra = 1

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'locationtype', 'planet')

class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemResourceInline,)

admin.site.register(Planet, PlanetAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Resource)
admin.site.register(Item, ItemAdmin)
