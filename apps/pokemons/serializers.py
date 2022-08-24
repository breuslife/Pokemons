from rest_framework import serializers

from pokemons.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'description', 'height', 'weight', 'order']
