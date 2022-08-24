from django.contrib import admin

from pokemons.models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['pk', '_get_name', '_get_height', '_get_weight', 'order']
    list_display_links = ['pk', '_get_name']
    ordering = ('pk',)
    list_per_page = 25

    def _get_name(self, obj):
        return f'{obj.name}'.capitalize()
    _get_name.short_description = 'Name'

    def _get_height(self, obj):
        return f'{obj.height / 10} m'
    _get_height.short_description = 'Height'

    def _get_weight(self, obj):
        return f'{obj.weight / 10} kgs'
    _get_weight.short_description = 'Weight'
