import requests
import random
def random_pokemon():
    id_list = range(1, 52)
    id = random.choice(id_list)
    return id

def api_call():
    url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon()}/'
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'].capitalize(),
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']
    }


api_call()


