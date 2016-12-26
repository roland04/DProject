from django.contrib import admin

from .models import Character, Attribute, Skill, CharacterAttribute, CharacterSkill, ShipModel, Ship

class CharacterAttributeInline(admin.TabularInline):
    model = CharacterAttribute
    extra = 1

class CharacterSkillInline(admin.TabularInline):
    model = CharacterSkill
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    inlines = (CharacterAttributeInline,CharacterSkillInline,)

admin.site.register(Skill)
admin.site.register(Attribute)
admin.site.register(Character, CharacterAdmin)
admin.site.register(ShipModel)
admin.site.register(Ship)
