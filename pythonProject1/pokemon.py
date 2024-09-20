import requests
import random


def api_call(id):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'].capitalize(),
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']
    }





