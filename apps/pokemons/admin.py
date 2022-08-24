from django.contrib import admin

from pokemons.models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    """For future customizations"""

