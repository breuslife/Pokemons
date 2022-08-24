import requests
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from app import settings

from pokemons.models import Pokemon
from pokemons.serializers import PokemonSerializer
from pokemons.pagination import PokemonSetPagination


API_POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
API_POKEMONS_URL = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1154'  # Get all Pokemons


class PokemonView(ModelViewSet):
    """Main Pokémon API method"""

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    pagination_class = PokemonSetPagination

    def create(self, request, *args, **kwargs):
        r = requests.get(API_POKEMONS_URL)
        pokemons = r.json()['results']  # Get all Pokemons (1154)

        for pokemon_data in pokemons:
            pokemon_url = pokemon_data['url']
            pokemon = requests.get(pokemon_url).json()

            Pokemon.objects.update_or_create(
                name=pokemon.get('name'),
                height=pokemon.get('height', None),
                weight=pokemon.get('weight', None),
                order=pokemon.get('order', 0),
            )
        return Response(data=response, status=201)
