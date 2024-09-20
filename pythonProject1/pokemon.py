import requests
import random
def random_pokemon():
    id_list = range(1, 52)
    id = random.choice(id_list)
    return id

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


def play():
    player_pokemon_id = random_pokemon()
    player_pokemon = api_call(player_pokemon_id)

    bot_pokemon_id = random_pokemon()
    bot_pokemon = api_call(bot_pokemon_id)

    print(f'Your pokemon is {player_pokemon['name']}'),
    print(f'Bot pokemon is {bot_pokemon['name']}'),


play()







